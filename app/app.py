from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "new post", "content": "cool test post"},
    2: {"title": "Morning thoughts", "content": "Today feels like a good day to start something new."},
    3: {"title": "Weekend plans", "content": "Thinking about going out with friends this weekend."},
    4: {"title": "Coding update", "content": "Finally fixed that annoying bug after an hour of debugging."},
    5: {"title": "Good music", "content": "Found a new playlist and now I can't stop listening to it."},
    6: {"title": "College life", "content": "Assignments are piling up, but we move."},
    7: {"title": "Random question", "content": "What's one skill everyone should learn at least once?"},
    8: {"title": "Late night", "content": "Why do all the best ideas show up at 2 AM?"},
    9: {"title": "Small wins", "content": "Made a little progress today, and that's enough for me."},
    10: {"title": "Food debate", "content": "Pizza or burgers? Honestly, depends on the mood."},
    11: {"title": "Monday motivation", "content": "You don't need to have everything figured out. Just keep going."}
}

@app.get("/posts")
def get_all_posts(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title" : post.title, "content":post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

