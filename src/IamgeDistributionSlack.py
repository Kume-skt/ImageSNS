import matplotlib.pyplot as plt
import numpy as np
import requests
import io

rand = np.random.RandomState(42)

mean = [0, 0]
cov = [[1, 2], [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)

fig = plt.figure()
plt.scatter(X[:, 0], X[:, -1])


format = "png"
sio = io.BytesIO()
plt.savefig(sio, format=format)

plt.close(fig)

# slackのアクセストークン
accessToken = "xoxb-000000000-000000000-HOGEHOGEHOGEHOGE"
channel_id = "ABCDEFG"

files = {'file': ("test", sio.getvalue(), "text/tab-separated-values")}
data = {'token': accessToken, 'channels': channel_id,
        "title": "test",
        "filename": "test",
        "filetype": "png"
        }

res = requests.post(url="https://slack.com/api/files.upload",
                    data=data, files=files)
print(res.content)
