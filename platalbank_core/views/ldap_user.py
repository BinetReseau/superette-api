import ldap
from django.http import JsonResponse


def make_ldap_query(filter):
    con = ldap.initialize('ldap://frankiz.eleves.polytechnique.fr', bytes_mode=False)
    return con.search_s('dc=frankiz,dc=net', ldap.SCOPE_SUBTREE, filter)


def attribute_getter(x, attribute):
    if attribute in x[1]:
        return x[1][attribute][0].decode("UTF-8")
    return None


def get_users_by_uid(uid_substring, promo=None, platal=None):
    opt1 = opt2 = ""
    if promo:
        opt1 = "(brPromo=" + str(promo) + ")"
    if platal:
        opt2 = "(brMemberOf=on_platal)"

    results = make_ldap_query("(&(uid=*" + uid_substring + "*)" + opt1 + opt2 + ")")
    if len(results) == 0:
        return []
    results = list(map(lambda x: {
                            'uid': attribute_getter(x, "uid"),
                            'firstname': attribute_getter(x, "givenName"),
                            'lastname': attribute_getter(x, "sn"),
                            'mail': attribute_getter(x, "mail"),
                            'phone': attribute_getter(x, "brPhone"),
                            'room': attribute_getter(x, "brRoom"),
                            'promo': attribute_getter(x, "brPromo"),
                             }, results))
    return results


def ldap_search(request):
    q = request.GET.get("q")
    platal = request.GET.get("platal")
    promo = request.GET.get("promo")
    users = []
    if q and len(q) > 0:
        try:
            users = get_users_by_uid(q, promo=promo, platal=platal)
        except ldap.SIZELIMIT_EXCEEDED:
            return JsonResponse({"error": "Size limit exceeded. Try a narrower research"})
    return JsonResponse({"users": users})
