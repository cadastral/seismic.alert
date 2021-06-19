#%%
import json
import requests

from toolz import groupby

from icecream import ic

# %%


def get_posts():
    response = requests.request("GET", "http://seismic-alert.ro/posts.json")
    response.raise_for_status()

    return json.loads(response.content)


# %%
posts = get_posts()

with open("posts.json", "w", encoding="utf-8") as fh:
    json.dump(posts, fh, sort_keys=True, indent=2, ensure_ascii=False)

print("== DONE ==")

# %%

ic(len(posts))

by_class = groupby(lambda p: p["active_submission"]["seismic_class"]["name"], posts)

ic({k: len(v) for k, v in by_class.items()})


# %%
ic(538 + 183 + 312 + 91 + 7 + 314 + 600 + 667 + 169 + 1)

# %%
