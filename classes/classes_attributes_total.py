class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0 
        Comment.total_comments += 1


first_comment = Comment("First comment")
print(Comment.total_comments)

second_comment = Comment("Second comment")
print(Comment.total_comments)
first_comment.total_comments = 10

print(Comment.total_comments)
print(first_comment.total_comments)
print(Comment.total_comments)

Comment.total_comments = 10 
print(Comment.total_comments)
print(first_comment.total_comments)