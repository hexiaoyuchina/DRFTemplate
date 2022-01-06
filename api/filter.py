from django.db.models import Q


def douban_search(queryset, value):
    if not value:
        return queryset
    queryset = queryset.filter(Q(title__icontains=value) or Q(country__icontains=value))
    return queryset