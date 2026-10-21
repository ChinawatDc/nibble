from api.utils.paginate import paginate

def handler(req, db):
    return paginate(db.all(), int(req.get('page', 1)))
