import requests
import time
from .models import SiteUrl
import csv
from datetime import datetime


def check_response(result, url):
    t1 = time.time()
    response = requests.get(url)
    t2 = time.time()-t1
    objs = SiteUrl.objects.filter(**{'url_address': url[8:]})

    if len(list(objs)) == 0:
        SiteUrl.objects.create(
            url_address=url[8:],
            page_name=url[8:].split('/')[1] + '_' + url[8:].split('/')[2],
            status=response.status_code,
            last_update=datetime.now(),
        )
    else:
        obj = objs[0]
        time_till_change = 0
        if obj.status == response.status_code:
            time_delta = datetime.now() - obj.last_update
            time_till_change = time_delta.total_seconds()
        obj.update(
                status=response.status_code,
                last_update=datetime.now(),
                time_till_change=time_till_change,
        )
        obj.save()




