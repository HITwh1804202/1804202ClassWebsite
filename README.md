# 前言

* vue不是很难，有事问度娘就o了
* 一定要看一下html和css
* 作者：康国健

# 拉取配置完成的vue工程目录

1. 下载sourcetree，安装
2. 克隆master分支
3. 用sourtree打开工程目录，Add->浏览->起名->添加
4. 点分支->创建分支->起名->指定的提交->选择**绑定路由，简要设置header和footer，更新README.md文档**这个->确定->创建分支
5. 在文件资源管理器中打开，打开终端
6. 确保安装nodejs和cnpm
7. `cnpm install`
8. `npm run serve` 运行
9. 浏览器访问`http://localhost:8080/`，即可实时预览网页内容。**代码保存网页自动更新**
10. ctrl+c可以停止项目

# 工程目录结构详解

```
|--node_modules                               //这个是npm安装的依赖，cnpm install后出现，git上没有
|--public                                     //入口文件目录
|    |--favicon.ico                           //vue的icon图标
|    |--index.html                            //入口文件
|--src                                        //源代码文件目录
|    |--assets                                //静态文件目录，包含一些图片等
|    |--components                            //组件目录，欲了解组件写法，看vue文档的单元件组件
|    |--plugins                               //插件目录
|    |     |--element.js                      //实际上这个js可以并入main.js，这个是elementui的引入js文件
|    |--router                                //路由目录
|    |     |--index.js                        //路由配置文件，配置页面跳转
|    |--store                                 //Vuex目录
|    |     |--index.js                        //Vuex配置文件，配置一些全局数据
|    |--styles                                //全局样式目录
|    |     |--element-variables.scss          //elementui的样式文件
|    |     |--main.scss                       //默认样式，为了覆盖vue自带的一些样式
|    |--views                                 //界面目录
|    |     |--announce                        //公告板界面模块，包含一些和公告板有关的界面
|    |     |    |--index.vue                  //公告板主界面
|    |     |    |--otherpage.vue              //公告板其他界面
|    |     |--download                        //资源下载界面模块，包含一些和资源下载有关的界面
|    |     |    |--index.vue                  //资源下载主界面
|    |     |    |--otherpage.vue              //资源下载其他界面
|    |     |--index                           //主页界面模块，包含一些和主页有关的界面
|    |     |    |--index.vue                  //主页主界面
|    |     |    |--otherpage.vue              //主页其他界面
|    |     |--message                         //留言板界面模块，包含一些和留言板有关的界面
|    |     |    |--index.vue                  //留言板主界面
|    |     |    |--otherpage.vue              //留言板其他界面
|    |--App.vue                               //二级入口文件
|    |--main.js                               //网站配置文件，引入其他组件，初始化vue
|--.gitignore                                 //将文件或目录写入后，git不会将其提交
|--babel.config.js                            //没查这是干啥的_φ(❐_❐✧)φ_
|--package-lock.json                          //npm所有依赖的详细信息
|--package.json                               //npm安装的工程组件
|--README.md                                  //说明文档
|--vue.config.js                              //workpack与vue混合超级配置文件，修改后重启项目生效

```

# 开发简介

#### 1. `.vue`文件

* `.vue`文件是vue的模板文件，一个vue文件绑定一层路由，一般用于一个界面，但是可以结合路由实现页面的嵌套。

```html
<!--模板结构-->

<!--这相等于html的部分，注意template标签中必须有一个大的div标签-->
<template>
  <div id="announce">这是公告栏主页</div> <!--比如这个-->
</template>

<!--这是js的部分，需要看vue的文档-->
<script>
export default {
    name:"announce",
    data(){ //数据
        return {
            index:1,
        }
    },
    method:{
        //函数部分
    },
    mounted(){
        //这是一个周期函数，页面加载时自动执行代码
    }
}
</script>

<!--这是样式的部分，scoped表示下列样式只用于该vue文件，不加的话，所有vue文件都会生效-->
<style lang="scss" scoped>
#announce{

}
</style>
```

#### 2.`main.js`文件

* 通过import引入js文件，css/scss/less样式文件，引入插件，引入组件。这是全局引入
* 也可以在vue文件的script标签内全局引入
* script标签不能引入网络cdn

#### 3.路径问题

* @表示./src/下的根目录，比如在任何地方引入assets中的icon.png文件，可用路径`"@assets/icon.png"`

#### 4.router路由

* 服务器访问url为`http://localhost:8080/`，访问此地址会重定向到`http://localhost:8080/#/`。
* #后面的路径是路由绑定的模板文件（vue文件）

```js
//第一种绑定方式
{
    path:'/', //绑定#后面的/页面
    name:'Index',
    component:() => import(/* webpackChunkName: "about" */ '../views/index/index.vue')//第一种绑定方式
}
```

```js
//第二种绑定方式
import Index from '../views/index/index.vue'
```

```js
{
    path:'/', //绑定#后面的/页面
    name:'Index',
    component:Index
}
```

* 实际上我们一般这样绑定

```js
import Index from '../views/index/index.vue'

const routes = [
  {
    path: '/',
    redirect:'/index' //重定向，只要访问“/”就会转到“/index”
  },
  {
    path: '/index', //绑定#后面的/index页面
    name: 'Index',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:Index
  }
]

```

* 子路由

```js
{
    path: '/index',
    name: 'Index',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:import(/* webpackChunkName: "about" */ '../views/index/index.vue'),
    children:[
        //该子路由的url为#/index/otherpage.vue
        {
            path:"otherpage",
            name:"Otherpage",
            component:import(/* webpackChunkName: "about" */ '../views/index/Otherpage.vue')
        }
    ]
}
//那么#后的/index/otherpage就绑定到了../views/index/Otherpage.vue页面内
```

* 下面是两个vue的标签

```html
<!--这个是跳转标签-->
<router-link :to="这里写页面地址或者页面名称，比如:/index或者Index">
    此处可以填写文字等
</router-link>
<!--它就相当于一个超链接标签，只不过它可以使用你所绑定的路由-->
```

```html
<!--这个是路由标签-->
<!--详细讲解此标签-->
<router-view/>
<!--
    1.它可以出现在任何页面
    2.绝大多数情况下App.vue中会有一个<router-view/>，除非是单页面网站
    3.首先要了解vue项目的页面渲染过程：
        <1>.比如访问message下的index.vue页面
        <2>.这个页面绑定的url为#/message，#前面省略
        <3>.从我们的角度看，我们看见的页面实际上位于项目根目录的public下的index.html文件，它看上去像空的，并且不需要我们改动
        <4>.项目运行时，vue会将App.vue塞到index.html给我们看，从这一点可以看到，App.vue文件中的所有组件，我们在所有界面都可以看到
        <5>.如果没有<router-view/>，我们只能看到App.vue的界面
        <6>.加上<router-view/>之后，<router-view/>就会被#/message绑定的页面，也就是message下的index.vue页面代替，就是塞进来
    4.那我们加上子路由
        <1.if #/message 绑定的页面中存在<router-view/>>
            那么#/message/otherpage.vue绑定的页面就会替换掉#/message所绑定页面中的<router-view/>
        <1.if #/message 绑定的页面中不存在<router-view/>>
            那么#/message/otherpage.vue绑定的页面就会替换掉App.vue中的<router-view/>
    5.仔细看上面的说明，并且测试，就能很简单的掌握，看不懂的可以找我求助，或者找度娘求助
-->
```

* 对于elementui的用法，访问
* `https://element.eleme.cn/#/zh-CN/component/installation`
* 寻找组件并且复制粘贴
* 请求后端需要用到axios，请百度并且尝试自行安装。