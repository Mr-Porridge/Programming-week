<template>
  <el-container>
    <el-header>留言板</el-header>
    <el-container>
      <el-aside width="210px">
        <sidebar style="width: 211px"></sidebar>
      </el-aside>
      <el-main>
        <el-dialog title="确认解密" :visible.sync="dialogFormVisible">
          <el-form>
            <el-form-item label="请输入密码" :label-width="formLabelWidth">
              <el-input v-model="password" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="confirmDecode()">确 定</el-button>
          </div>
        </el-dialog>
        <!--message box begin-->
        <div class="message-box">
          <el-carousel :interval="4000" type="card" height="200px" trigger="click">
            <el-carousel-item v-for="item in leavedMessages" :key="item.id">
              <div @click="decodeText(item.mes)">
                <el-tag
                  type="info"
                  effect="plain"
                  style="margin-top: 3px; margin-left: 3px"
                >To: {{ item.friend }}
                </el-tag>
                <el-input
                  class="box-card"
                  :disabled="true"
                  type="textarea"
                  :autosize="{ minRows: 4, maxRows: 7}"
                  v-model=item.mes
                ></el-input>
                <!--<el-card class="box-card">
                  <div>
                    {{item.mes }}
                  </div>
                </el-card>-->
              </div>
            </el-carousel-item>
          </el-carousel>
        </div>
        <!--message box end-->

        <!--message content begin-->
        <div style="margin: 5px">
          <el-form :inline="true" class="demo-form-inline" label-width="120px" label-position="left">
            <el-form-item label="快给朋友留言吧">
              <el-input v-model="friendName" placeholder="To: your friend name here" clearable></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="encodeText()">加密</el-button>
            </el-form-item>
            <el-form-item style="padding-left: 43%">
              <el-button type="primary" @click="saveMessage()">确定留言</el-button>
            </el-form-item>
          </el-form>
        </div>
        <div style="margin: 5px;">
          <el-form label-position="left" label-width="120px">
            <el-form-item label="内容">
              <el-input type="textarea"
                        :autosize="{ minRows: 3, maxRows: 8}"
                        v-model="userInput"
                        placeholder="Please input you message here in English (CAPITAL FORM)"></el-input>
            </el-form-item>
          </el-form>
          <!--message content begin-->
        </div>
        <div style="margin: 5px;">
          <el-form label-position="left" label-width="120px">
            <el-form-item label="密文">
              <el-input type="textarea"
                        :autosize="{ minRows: 4, maxRows: 8}"
                        v-model="ans"
                        placeholder="Please click encode button to encode the message."></el-input>
            </el-form-item>
          </el-form>
          <!--message content begin-->
        </div>

      </el-main>
    </el-container>
  </el-container>
</template>

<script>
    import sidebar from '@/components/sidebar/'
    import axios from 'axios'
    import qs from "qs"
    import Sidebar from "../../components/sidebar/index";

    export default {
        components: {Sidebar},
        component: {sidebar},
        name: 'message_board',
        data() {
            return {
                friendName: "",
                userInput: "",
                ans: "",
                plainMes: "",
                leavedMessages: [
                    {
                        id: 0,
                        friend: "Tony",
                        mes: "1100011",
                    },
                    {
                        id: 1,
                        friend: "Susan",
                        mes: "110001101010100111001001001111001110010",
                    },
                    {
                        id: 2,
                        friend: "Mike",
                        mes: "1101010100111000110101010011100100100111",
                    },
                    {
                        id: 3,
                        friend: "Harry",
                        mes: "1110101010011000110101010011100100100111",
                    },
                    {
                        id: 4,
                        friend: "Hermione",
                        mes: "1100011101010100110101010011100100100111",
                    },
                    {
                        id: 5,
                        friend: "Granger",
                        mes: "110101010011111010101001000110101010011100100100111",
                    },
                ],
                password: "",
                dialogFormVisible: false,
                formLabelWidth: '120px',
            };
        },
        methods: {
            translate(code) {
                console.log(code);
            },

            encodeText() {
                console.log("加密中........");
                console.log("用户输入:", this.userInput);
                const userInputData = {
                    "friend_name": this.friendName,
                    "user_input": this.userInput,
                };
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/huffman_encode/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.ans = res.data;
                });
            },

            saveMessage() {
                console.log("保存留言中........");
                console.log("留言明文:", this.userInput);
                const userInputData = {
                    "friend_name": this.friendName,
                    "user_input": this.userInput,
                    "encoded_text": this.ans,
                };
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/message_save/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    console.log(res.data);
                    this.friendName = this.userInput = this.ans = "";
                    this.alert("留言成功！");
                });
            },

            messageLoad() {
                console.log("加载留言中........");
                const userInputData = {"JUST": "GET"};
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/message_load/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.leavedMessages = res.data;
                    console.log(this.leavedMessages);
                });
            },

            decodeText(binaryMes) {
                this.dialogFormVisible = true;
                console.log("解密中........");
                console.log("解密内容:", binaryMes);
                const userInputData = {"user_input": binaryMes};
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/huffman_decode/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.plainMes = res.data;
                });
            },

            confirmDecode() {
                this.dialogFormVisible = false;
                this.password = "";
                this.$notify({
                    title: '解密成功！',
                    message: this.plainMes,
                    type: 'success'
                });
            }
        },
        mounted() {
            this.messageLoad()
        }
    }
</script>

<style scoped>
  .el-header {
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

  .el-carousel__item h3 {
    text-align: center;
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .box-card {
    cursor: pointer;
    background-color: #99a9bf;
    font-size: 20px;
    margin-top: 10px;
    margin-left: 3px;
    width: 98%;
    height: 100%;
  }


  .box-card:hover {
    cursor: pointer;
    background-color: #99a9bf;
    font-size: 30px;
    margin-top: 15px;
    margin-left: 4px;
    margin-right: 4px;
    width: 98%;
    height: 100%;
  }
</style>
