# js异步请求
# 一些后端语言的框架如django是把变量渲染到html模板最终在response返回，用户交互式需要刷新页面才能看到休修改后的效果。为了更好的网页体验和前后端程序员工作分离。前端js工作中也有类似后端requests包的前端操作包。导致有些数据第一次html中并看不到,浏览器会在加载html后执行js，但requests包不会，无法直接


"""
<html>
    <body>
        <h1>带爬取内容</h1>
        <script>
            function foo():{
                //请求商品列表
                //操作dom节点把商品信息渲染到页面中。
            })
        </script>
    </body>
</html>
"""
"""
需求：爬取京东一个商品评论







"""