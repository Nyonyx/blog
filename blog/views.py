from datetime import date
from django.shortcuts import render

posts_items = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in te mountains! And I wasn't even prepared for what happened whilst I was enjoying the views !",
        "content": """ 
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus convallis dapibus consectetur. Suspendisse et congue ante, at aliquet nisl. Nunc sed nulla vitae enim gravida egestas.
            Aenean vestibulum feugiat luctus. Aliquam congue ornare metus, vitae scelerisque nunc posuere eu. Vestibulum tristique enim sed nulla elementum,
            eu dapibus magna porttitor. Praesent cursus lacinia dui at tincidunt. Duis tincidunt vitae sem vel ornare. 
            Suspendisse eleifend turpis ac sapien cursus vestibulum. 
            Proin dapibus laoreet magna feugiat laoreet. 
            Pellentesque in ultrices arcu.
            Ut suscipit lectus velit, quis dapibus enim gravida non."
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post.get('date')

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(posts_items, key=get_date, reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": posts_items
    })

def post_detail(request, slug):
    identified_post = next(post for post in posts_items if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })