import pymongo

from database import Database
from models.blog import Blog



Database.initialize()

blog = Blog(author="Robin",
            title = 'Tavu',
            description="bien")

blog.new_post()
print("NEw post done")
blog.save_to_mongo()
print('The blog has been saved')
from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())