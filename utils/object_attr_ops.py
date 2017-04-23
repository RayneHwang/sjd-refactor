from models.SJD_USER import SjdUser


def update_obj_attr(obj, attr_dict):
    if attr_dict is not None:
        for attr in obj.__dict__:
            if attr in attr_dict:
                setattr(obj, attr, attr_dict.get(attr))
    else:
        return


def get_ordinary_fields(obj):
    res = {}
    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
        res[field] = getattr(obj, field)
    return res


def mask_pass(i):
    if isinstance(i, dict):
        if i['password'] is not None:
            i['password'] = 'xxxxxx'
    else:
        if getattr(i, 'password') is not None:
            setattr(i, 'password', 'xxxxxx')
    return i


if __name__ == '__main__':
    user1 = SjdUser(username='sasa', password='1223')
    user2 = {'username': 'sasa', 'password':'1223'}
    print(mask_pass(user1).password)
    print(mask_pass(user2)['password'])
