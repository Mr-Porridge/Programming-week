<template>
  <el-container>
    <el-header>判断二叉树是否为二叉平衡树
    </el-header>
    <el-container>
      <el-aside width="210px">
        <sidebar style="width: 211px"></sidebar>
      </el-aside>
      <el-main>
        <!--<el-button type="primary" style="margin:0 0 3% 85%" @click="changeMethod()" v-if="inputMethod===true">文本输入方式
        </el-button>-->
        <el-button type="primary" style="margin:0 0 3% 85%" @click="changeMethod()" v-if="inputMethod===false">图形输入方式
        </el-button>
        <div v-if="inputMethod === true">
          <el-container class="checking">
            <div style="margin: 5px">
              <el-form :inline="true" class="demo-form-inline" label-width="120px" label-position="left">
                <el-form-item label="输入构建二叉树">
                  <el-input v-model="userInput" placeholder="请输入字符串"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="isBalanced()">判断</el-button>
                </el-form-item>
              </el-form>
            </div>
          </el-container>
          <el-container class="checking">
            <div style="margin: 5px;">
              <el-form label-position="left" label-width="120px">
                <el-form-item label="二叉搜索树">
                  <el-input v-model="balanced.binarySearchTree" placeholder="点击判断按钮查看结果"></el-input>
                </el-form-item>
                <el-form-item label="二叉平衡树">
                  <el-input v-model="balanced.balancedBinaryTree" placeholder="点击判断按钮查看结果"></el-input>
                </el-form-item>
              </el-form>
            </div>
          </el-container>
        </div>
        <div v-if="inputMethod === false">
          <el-container class="checking">
            <div style="margin: 5px;">
              <el-form label-position="left" label-width="120px">
                <el-form-item label="二叉搜索树">
                  <el-input v-model="balanced.binarySearchTree" placeholder="点击判断按钮查看结果"></el-input>
                </el-form-item>
                <el-form-item label="二叉平衡树">
                  <el-input v-model="balanced.balancedBinaryTree" placeholder="点击判断按钮查看结果"></el-input>
                </el-form-item>
              </el-form>
            </div>
          </el-container>
        </div>
        <el-button type="primary" style="margin:7% 0 0 0" @click="show">展示图形</el-button>
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
    import $ from 'jquery'

    export default {
        components: {Sidebar},
        component: {sidebar},
        name: 'balanced',
        data() {
            return {
                inputMethod: true,
                userInput: '',
                balanced: {
                    binarySearchTree: '',
                    balancedBinaryTree: '',
                }
            };
        },
        methods: {
            isBalanced() {
                console.log("判断中........");
                console.log("用户输入:", this.userInput);
                const userInputData = {"user_input": this.userInput};
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/balanced_binary_tree/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.balanced.binarySearchTree = res.data[0];
                    this.balanced.balancedBinaryTree = res.data[1];
                }).catch(function (err) {
                    console.log(err);
                });
            },
            changeMethod() {
                this.inputMethod = !this.inputMethod;
            },
            show() {
                console.log("At this time: ", this.userInput);
                this.$router.push({
                    path: '/tree',
                    name: 'tree',
                    params: {userText: this.userInput},
                });
            },
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
    height: 800px;
  }

  .checking {
    width: 500px;
    height: 60px;
  }

  .el-row {
    margin-bottom: 20px;

  }

  :last-child {
    margin-bottom: 0;
  }

  .el-col {
    border-radius: 4px;
  }

  .bg-purple-dark {
    background: #99a9bf;
  }

  .bg-purple {
    background: #d3dce6;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
