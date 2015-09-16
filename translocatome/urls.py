from django.conf.urls import patterns

urlpatterns = patterns('translocatome.api',
                       (r'api/interaction/fields/$', 'interaction_fields'),
                       )

urlpatterns += patterns('translocatome.rest_api',
                        (r'rest-api/query-nodes/$', 'query_nodes'),
                        (r'rest-api/query-interactions/$', 'query_interactions'),
                        (r'rest-api/node/$', 'node'),
                        (r'rest-api/node/(?P<node_id>[0-9]+)/$', 'node'),
                        (r'rest-api/interaction/$', 'interaction'),
                        (r'rest-api/interaction/(?P<interaction_id>[0-9]+)/$', 'interaction'),
                        )
