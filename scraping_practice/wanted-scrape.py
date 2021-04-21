import requests
import json
import requests

headers = {
    'authority': 'www.wanted.co.kr',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'wanted-user-country': 'KR',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ3YW50ZWQiLCJpYXQiOjE2MTg4ODkzODcsInVzZXJfaWQiOjE3NDQyNjYsImlzX2FkbWluIjpmYWxzZSwicHJvdmlkZXIiOiJnb29nbGUifQ.CWAuDEFAQ9K-mm9HlqHLrnA8o2KUJbT6b2tSCZ3GGjU',
    'accept': 'application/json, text/plain, */*',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'wanted-user-language': 'ko',
    'wanted-user-agent': 'user-web',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.wanted.co.kr/',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'uuid=4959-3d19-2dac-d4f4; _gcl_au=1.1.1079805841.1617548068; ab.storage.deviceId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%229fe8b323-fabc-49cc-a7f0-c1854e6d7626%22%2C%22c%22%3A1617548068466%2C%22l%22%3A1617548068466%7D; _fbp=fb.2.1617548073255.1665159544; _gid=GA1.3.1189720661.1618889316; clickKey=; wtd-joblist-count=5; login_type=google; onboarding_redirect_url=/wdlist/513/10145; before_url=https://www.wanted.co.kr/onboarding?should=/wdlist/513/10145; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ3YW50ZWQiLCJpYXQiOjE2MTg4ODkzODcsInVzZXJfaWQiOjE3NDQyNjYsImlzX2FkbWluIjpmYWxzZSwicHJvdmlkZXIiOiJnb29nbGUifQ.CWAuDEFAQ9K-mm9HlqHLrnA8o2KUJbT6b2tSCZ3GGjU; remember_token=1744266|a8053d117554386892bffb4720758c8141aafdbe; ab.storage.userId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%221744266%22%2C%22c%22%3A1618889389182%2C%22l%22%3A1618889389182%7D; AWSALBTG=6FMc3HHhvOrxoOGoUXCU/sYUrB7KtjGLq49gFaLC1LMP6u/vjLOMBSNePXx6e+rU/O6/9RTSOPS3Qp1dA/DYypEcnDK9/fhqNVTZuyO4l/zYWq1eLgiVEnYgURbtqTKrlqyhFRyM2OrZtdisPhEvNZy5lc+v8pDbVz71gVgSuske3syPnNY=; AWSALBTGCORS=6FMc3HHhvOrxoOGoUXCU/sYUrB7KtjGLq49gFaLC1LMP6u/vjLOMBSNePXx6e+rU/O6/9RTSOPS3Qp1dA/DYypEcnDK9/fhqNVTZuyO4l/zYWq1eLgiVEnYgURbtqTKrlqyhFRyM2OrZtdisPhEvNZy5lc+v8pDbVz71gVgSuske3syPnNY=; AWSALB=acDvNTVk3h6HQAMQK5rxclM0IfkwQ+v+YkJL+Wpku0vzVtjAnH5dvZ4gjUIM1/4lPhqrb+XirRNR4aoc85KhIgiBQf21CKZRleFPfb3brWk0u2WVcn5UlJS0hmBm; AWSALBCORS=acDvNTVk3h6HQAMQK5rxclM0IfkwQ+v+YkJL+Wpku0vzVtjAnH5dvZ4gjUIM1/4lPhqrb+XirRNR4aoc85KhIgiBQf21CKZRleFPfb3brWk0u2WVcn5UlJS0hmBm; ab.storage.sessionId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%22d497fd20-1464-d0b8-ba29-9cf545b7cfd7%22%2C%22e%22%3A1618903849338%2C%22c%22%3A1618898128549%2C%22l%22%3A1618902049338%7D; utm=; amplitude_id_d08dcdfb83963e2b5a1d4500f246aa92wanted.co.kr=eyJkZXZpY2VJZCI6IjdlOThmMmMwLTRhN2MtNDZlMS1hMWVkLWJlMmI2YTMwODVlM1IiLCJ1c2VySWQiOiIxNzQ0MjY2Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjE4ODk2OTg2MTQ2LCJsYXN0RXZlbnRUaW1lIjoxNjE4OTAyMDUwMzQzLCJldmVudElkIjoxMjcsImlkZW50aWZ5SWQiOjY2LCJzZXF1ZW5jZU51bWJlciI6MTkzfQ==; _ga=GA1.1.740790566.1617548069; wcs_bt=s_133d2f67e287:1618902051; _ga_YKFMYZ2YXR=GS1.1.1618896695.4.1.1618902292.0; _ga_4XX1N5VVJ2=GS1.1.1618896695.4.1.1618902292.0; session=eyJfZnJlc2giOmZhbHNlLCJfaWQiOnsiIGIiOiJObUkyT0dJMFptSmpZamRoTm1Ka05qZzBPV1V4TldVM01qaGtNRE0zWldZPSJ9LCJpcCI6IjEwNi4yNDIuNzkuMjMwIiwibGFuZyI6ImtvIiwidXNlcl9pZCI6IjE3NDQyNjYifQ.E2AOuw.HMao4iOupcP38qZswFKZIhS7ToY',
}

jobs = []
for offset in range(0, 100+1, 20):
    params = (
        ('1618902340096', ''),
        ('country', 'kr'),
        ('tag_type_id', '872'),
        ('job_sort', 'job.latest_order'),
        ('locations', 'all'),
        ('years', '0'),
        ('limit', '20'),
        ('offset', f'{offset}'),
    )

    response = requests.get('https://www.wanted.co.kr/api/v4/jobs', headers=headers, params=params)
    

    for i in range(len(response.json()["data"])):
        jobs.append({"id": response.json()["data"][i]["id"], "position":response.json()["data"][i]["position"]})

for job in jobs:
    
    print('\n\n','---------------', job["position"],'---------------')
    
    headers = {
        'authority': 'www.wanted.co.kr',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'wanted-user-country': 'KR',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ3YW50ZWQiLCJpYXQiOjE2MTg4ODkzODcsInVzZXJfaWQiOjE3NDQyNjYsImlzX2FkbWluIjpmYWxzZSwicHJvdmlkZXIiOiJnb29nbGUifQ.CWAuDEFAQ9K-mm9HlqHLrnA8o2KUJbT6b2tSCZ3GGjU',
        'accept': 'application/json, text/plain, */*',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        'wanted-user-language': 'ko',
        'wanted-user-agent': 'user-web',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.wanted.co.kr/',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'uuid=4959-3d19-2dac-d4f4; _gcl_au=1.1.1079805841.1617548068; ab.storage.deviceId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%229fe8b323-fabc-49cc-a7f0-c1854e6d7626%22%2C%22c%22%3A1617548068466%2C%22l%22%3A1617548068466%7D; _fbp=fb.2.1617548073255.1665159544; _gid=GA1.3.1189720661.1618889316; clickKey=; wtd-joblist-count=5; login_type=google; onboarding_redirect_url=/wdlist/513/10145; before_url=https://www.wanted.co.kr/onboarding?should=/wdlist/513/10145; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ3YW50ZWQiLCJpYXQiOjE2MTg4ODkzODcsInVzZXJfaWQiOjE3NDQyNjYsImlzX2FkbWluIjpmYWxzZSwicHJvdmlkZXIiOiJnb29nbGUifQ.CWAuDEFAQ9K-mm9HlqHLrnA8o2KUJbT6b2tSCZ3GGjU; remember_token=1744266|a8053d117554386892bffb4720758c8141aafdbe; ab.storage.userId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%221744266%22%2C%22c%22%3A1618889389182%2C%22l%22%3A1618889389182%7D; utm=; amplitude_id_d08dcdfb83963e2b5a1d4500f246aa92wanted.co.kr=eyJkZXZpY2VJZCI6IjdlOThmMmMwLTRhN2MtNDZlMS1hMWVkLWJlMmI2YTMwODVlM1IiLCJ1c2VySWQiOiIxNzQ0MjY2Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjE4ODk2OTg2MTQ2LCJsYXN0RXZlbnRUaW1lIjoxNjE4OTAxMTM1Njg1LCJldmVudElkIjoxMjIsImlkZW50aWZ5SWQiOjYzLCJzZXF1ZW5jZU51bWJlciI6MTg1fQ==; session=eyJfZnJlc2giOmZhbHNlLCJfaWQiOnsiIGIiOiJObUkyT0dJMFptSmpZamRoTm1Ka05qZzBPV1V4TldVM01qaGtNRE0zWldZPSJ9LCJpcCI6IjEwNi4yNDIuNzkuMjMwIiwibGFuZyI6ImtvIiwidXNlcl9pZCI6IjE3NDQyNjYifQ.E2AKEA.GydtCeuEk1OMi1GXCgT81qiB7yc; _ga=GA1.1.740790566.1617548069; wcs_bt=s_133d2f67e287:1618901136; _ga_YKFMYZ2YXR=GS1.1.1618896695.4.1.1618901217.0; _ga_4XX1N5VVJ2=GS1.1.1618896695.4.1.1618901217.0; AWSALBTG=XaiI2BPN3UrtPf2uncNLWzqkqUCuFMZHGfNOoc9XYsuSnKgIIsnt0kk/4fke+AZpxIiJPESBRoMjO0r6noQsaS9t9b4FfrF2iVpUJ9X13t7G3PRQADKm4a6IbP1KmTgnldH/+zggRztd+33VWkjDXH/LWp9guJTFp928YDxro+dEtbkvXlM=; AWSALBTGCORS=XaiI2BPN3UrtPf2uncNLWzqkqUCuFMZHGfNOoc9XYsuSnKgIIsnt0kk/4fke+AZpxIiJPESBRoMjO0r6noQsaS9t9b4FfrF2iVpUJ9X13t7G3PRQADKm4a6IbP1KmTgnldH/+zggRztd+33VWkjDXH/LWp9guJTFp928YDxro+dEtbkvXlM=; AWSALB=tifVK6pFw3p+vf+TAx94LrFazBTYhfE9XuwwQqwv8Mcwy5IY5za3J7XBIrljljY18gPROoMQnpj+9wpXqxrcxqT7Ic1f9nJp7MbwxhJq/PdjMgRx9PR+140STn53; AWSALBCORS=tifVK6pFw3p+vf+TAx94LrFazBTYhfE9XuwwQqwv8Mcwy5IY5za3J7XBIrljljY18gPROoMQnpj+9wpXqxrcxqT7Ic1f9nJp7MbwxhJq/PdjMgRx9PR+140STn53; ab.storage.sessionId.97672243-0e93-4d7d-890f-ea3507df4abe=%7B%22g%22%3A%22d497fd20-1464-d0b8-ba29-9cf545b7cfd7%22%2C%22e%22%3A1618903017552%2C%22c%22%3A1618898128549%2C%22l%22%3A1618901217552%7D',
    }

    params = (
        ('1618901217810', ''),
    )

    response = requests.get(f'https://www.wanted.co.kr/api/v4/jobs/{job["id"]}', headers=headers, params=params)
    print(response.json()["job"]["detail"]["requirements"])





