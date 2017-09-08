from  rest_framework.serializers import ModelSerializer,SerializerMethodField#,HyperlinkedIdentityField
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post

class PostListSerializer(ModelSerializer):
   # url = HyperlinkedIdentityField(
      #  view_name='posts_api:detail',
       # lookup_field='slug'
    #)
    user=SerializerMethodField()
    image=SerializerMethodField()
    class Meta:
        model=Post
        fields=[
     #       'url',
            'user',
            'title',
            'slug',
            'content',
            'publish',
            'image'

        ]

    def get_user(self,obj):
        return obj.user.username
    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PostDetailSerializer(ModelSerializer):
    #url='post_detail_url'
    user=SerializerMethodField()
    image=SerializerMethodField()
    class Meta:
        model=Post
        fields=[
     #       'url',
            'user'
            'title',
            'slug',
            'content',
            'publish',
            'image'
            'comments'

        ]
    def get_user(self,obj):
        return str(obj.user.username)
    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None
        return image
    def get_comments(self,obj):
        c_qs=Comment.objects.filter_by_instance(obj)
        comments=CommentSerializer(c_qs,many=True).data
        return comments
class PostCreateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'title',
            'slug',
            'content',
            'publish',
        ]