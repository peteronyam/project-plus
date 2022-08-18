# import requests
# import json
# import sys
#
#
# if len(sys.argv) != 2:
#     sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1000&term=" + sys.argv[1])
# to get explicit data from that api
# print(json.dumps(results.json(), indent=2))

# U = response.json()
# for result in U["results"]:
#     print(result["trackName"])

import sys
from bubble import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
