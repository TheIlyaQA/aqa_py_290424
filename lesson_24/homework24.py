from pony.orm import Database, Required, PrimaryKey, Set, db_session

db = Database()

class Item(db.Entity):
    id = PrimaryKey(int, auto=True)
    title_ua = Required(str)
    title_or = Required(str)
    type_src = Required(str)
    year = Required(str)
    director = Required(str)
    description = Required(str)
    poster = Required(str)
    json = Required(str)
    imdb = Required(str)
    link = Set("Link")

class Season(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(str)
    name = Required(str)
    season = Required(str)
    title = Required(str)
    link = Set("Link")

class Link(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(str)
    series_id = Required(str)
    quality = Required(str)
    its_work = Required(str)
    type_src = Required(str)
    m3u_link = Required(str)
    subs = Required(str)
    item = Required(Item)
    season = Required(Season)

db.bind(provider='sqlite', filename='uakino.db', create_db=True)

db.generate_mapping(create_tables=True)

@db_session
def check_in_base(entity_class, **kwargs):
    return entity_class.exists(**kwargs)

@db_session
def add_to_db(entity_class, **kwargs):
    entity_class(**kwargs)

@db_session
def add_m3u(link_id, m3u_link):
    link = Link[link_id]
    link.m3u_link = m3u_link

@db_session
def save():
    db.commit()