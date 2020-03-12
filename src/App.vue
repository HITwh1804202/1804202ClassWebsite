<template>
  <div id="app">
    <el-container>
      <el-header class="el-header">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo top-menu"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          :router="true"
        >
          <el-menu-item index="Index">首页</el-menu-item>
          <el-menu-item index="Announce">公告板</el-menu-item>
          <el-menu-item index="Message">留言板</el-menu-item>
          <el-menu-item index="Download">资源下载</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
      <el-footer class="el-footer" style="height: 200px;">
        <el-row :gutter="30" class="el-row-1">
          <el-col :span="6" class="el-col-1">
            <el-row :gutter="0"><i class="el-icon-message icon"></i>联系邮箱：*********@163.com</el-row>
            <el-row :gutter="0"><i class="el-icon-chat-round icon"></i>联系Q Q：***********</el-row>
            <el-row :gutter="0"><i class="el-icon-phone-outline icon"></i>联系电话：***********</el-row>
          </el-col>
          <el-col :span="18" class="el-col-2">
            <el-col :span="6">
              <el-row style="font-size: 20px;">首页</el-row>
              <el-row style="font-size: 10px;">进入首页</el-row>
              <el-row style="font-size: 10px;">登陆</el-row>
            </el-col>
            <el-col :span="6">
              <el-row style="font-size: 20px;">公告板</el-row>
              <el-row style="font-size: 10px;">查看公告</el-row>
              <el-row style="font-size: 10px;">发布公告</el-row>
            </el-col>
            <el-col :span="6">
              <el-row style="font-size: 20px;">留言板</el-row>
              <el-row style="font-size: 10px;">查看留言</el-row>
              <el-row style="font-size: 10px;">发布留言</el-row>
            </el-col>
            <el-col :span="6">
              <el-row style="font-size: 20px;">资料下载</el-row>
              <el-row style="font-size: 10px;">搜索资料</el-row>
              <el-row style="font-size: 10px;">资料上传</el-row>
            </el-col>
          </el-col>
        </el-row>
        <el-row :gutter="20" class="el-row-2">
          <el-col :span="24" style="font-size:10px;">
            Copyright © 2020-nowadays | powerd by 哈尔滨工业大学（威海）2018级信安二班
          </el-col>
        </el-row>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex:this.$route.name
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  },
  mounted(){
    //解决刷新后导航栏自动取消激活状态的问题
    let that = this;
    let href = window.location.href;
    console.log(href);
    console.log(href.split("/#/")[1]);
    that.activeIndex = href.split("/#/")[1];
  }
};
</script>

<style lang="scss" scoped>
#app {
  .el-header {
    padding: 0;
  }
  .el-footer {
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 0 50px 0 50px;
    background-color: #4b4b4b;
    color: #333;
    text-align: center;
    line-height: 70px;
    .el-row-1{
      padding:20px 0 20px 20px;
      color: white;
      .el-col-1{
        line-height: 30px;
        font-size: 15px;
        text-align: left;
        .icon{
          margin-right: 20px;
        }
      }
      .el-col-2{
        border-left-style:solid;
        border-left-width:1px;
        border-left-color:rgb(255, 255, 255);
        line-height: 30px;
        font-size: 15px;
      }
    }
    .el-row-2{
      border-top-style:solid;
      border-top-width:1px;
      border-top-color:rgb(255, 255, 255);
      color: white;
      .text{
        font-size: 10px;
      }
    }
  }
}
</style>
