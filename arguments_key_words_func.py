#def get_posts_info(name, posts_qty):
#    info = f"{name} wrote {posts_qty} posts"
#    return info
#info = get_posts_info(name='Vova', posts_qty=25)
#print(info)

def get_posts_info(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )
    return info
info = get_posts_info(name='Vova', posts_qty=25, id=1351)
print(info)