<template>
  <el-container>
    <el-header>密码本</el-header>
    <el-container>
      <el-aside width="210px">
        <sidebar style="width: 211px"></sidebar>
      </el-aside>
      <el-main>
        <el-radio-group v-model="dictionaryNumber" :change="showCodeBook()">
          <el-radio-button label="one"></el-radio-button>
          <el-radio-button label="two"></el-radio-button>
          <el-radio-button label="three"></el-radio-button>
          <el-radio-button label="four"></el-radio-button>
        </el-radio-group>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
    import sidebar from '@/components/sidebar/'
    import Mock from 'mockjs'
    import axios from 'axios'
    import qs from "qs"
    import Sidebar from "../../components/sidebar/index";

    export default {
        components: {Sidebar},
        component: {sidebar},
        name: 'encode',
        data() {
            return {
                dictionaryNumber: 'one',
                book: {},
            };
        },
        methods: {
            showCodeBook() {
                console.log("查询........");
                console.log("查询的密码字典为:", this.dictionaryNumber);
                const userInputData = {"user_input": this.dictionaryNumber};
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/cipher_book/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res.data);
                    this.ans = res.data
                });
            }
        }
    }
</script>

<style scoped>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #545c64;
    color: #333;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    height: 550px;
  }

  .checking {
    width: 500px;
    height: 60px;
  }
</style>
