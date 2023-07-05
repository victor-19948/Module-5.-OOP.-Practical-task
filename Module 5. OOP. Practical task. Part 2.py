import json


class Model:
    title = '1'
    text = '2'
    author = '3'

    def _save(self):
        a = dict()
        for i in list(filter(lambda x: not x.startswith('_'), dir(Model))):
            a[i] = getattr(Model, i, None)
        with open('filename.json', 'w') as f:
            json.dump(a, f)


Model()._save()
