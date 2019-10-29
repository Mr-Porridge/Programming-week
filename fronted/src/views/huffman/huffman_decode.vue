<template>
  <el-container>
    <el-header>哈夫曼解密</el-header>
    <el-container>
      <el-aside width="210px">
        <sidebar style="width: 211px"></sidebar>
      </el-aside>
      <el-main>
        <el-container class="checking">
          <div style="margin: 5px">
            <el-form :inline="true" class="demo-form-inline" label-width="120px" label-position="left">
              <el-form-item label="输入密文">
                <el-input v-model="userInput" type="textarea" autosize placeholder="请输入01串"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="decodeText()">解密</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-container>
        <el-container class="checking">
          <div style="margin: 5px;">
            <el-form label-position="left" label-width="120px">
              <el-form-item label="明文">
                <el-input type="textarea" autosize v-model="ans" placeholder="点击解密按钮进行解密"></el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-container>
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
                userInput: '',
                ans: '',
            };
        },
        methods: {
            decodeText() {
                console.log("解密中........");
                console.log("用户输入:", this.userInput);
                const userInputData = {"user_input": this.userInput};
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/huffman_decode/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.ans=res.data
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
