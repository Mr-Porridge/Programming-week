<template>
  <el-col>
    <el-menu
      :default-active=this.currentPage
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      route=true
    >
      <el-menu-item index="1">
        <i class="el-icon-cherry"></i>
        <span slot="title">A6-平衡二叉树</span>
      </el-menu-item>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-lock"></i>
          <span>B6-哈夫曼加密</span>
        </template>
        <el-menu-item-group>
          <template slot="title">加密</template>
          <el-menu-item index="2-1">创建字典</el-menu-item>
          <el-menu-item index="2-2">加密明文</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="解密">
          <el-menu-item index="2-3">查看字典</el-menu-item>
          <el-menu-item index="2-4">破译密码</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-menu-item index="3">
        <i class="el-icon-message"></i>
        <span slot="title">留言板</span>
      </el-menu-item>
      <!--<el-menu-item index="4">
        <i class="el-icon-magic-stick"></i>
        <span slot="title">Family Tree</span>
      </el-menu-item>-->
      <el-menu-item index="5">
        <i class="el-icon-setting"></i>
        <span slot="title">后台管理</span>
      </el-menu-item>

    </el-menu>
  </el-col>

</template>

<script>
    export default {
        name: "sidebar",
        data() {
            return {
                currentPage: '',
            }
        },
        methods: {
            //获取参数
            getSideBarActive() {
                //let urlParams = location.href.split("=")[1]; // 0 是前面的地址  1 为第一个参数 2 为第二个参数
                this.currentPage = this.$route.params.page;
                console.log(this.currentPage)
            },
            handleSelect(key) {
                switch (key) {
                    case '1':
                        this.$router.push({
                            path: '/balanced',
                            name: 'balanced',
                            params: {page: '1'},
                        });
                        break;
                    case '2-1':
                        this.$router.push({
                            path: '/balanced',
                            name: 'balanced',
                            params: {page: '2-1'},
                        });
                        break;
                    case '2-2':
                        this.$router.push({
                            path: '/encode',
                            name: 'encode',
                            params: {page: '2-2'},
                        });
                        break;
                    case '2-3':
                        this.$router.push({
                            path: '/dictionary',
                            name: 'dictionary',
                            params: {page: '2-3'},
                        });
                        break;
                    case '2-4':
                        this.$router.push({
                            path: '/decode',
                            name: 'decode',
                            params: {page: '2-4'},
                        });
                        break;
                    case '3':
                        this.$router.push({
                            path: '/message',
                            name: 'message',
                            params: {page: '3'},
                        });
                        break;
                    case '4':
                        this.$router.push({
                            path: '/tree',
                            name: 'tree',
                            params: {page: '4'},
                        });
                        break;
                    case '5':
                        window.location.href = "http://localhost:8000/admin";
                        break;

                }
            }
        },
        mounted: function () {
            this.getSideBarActive(); //加载时执行函数方法
        }
    }
</script>

<style scoped>

</style>
