<template>
  <el-container>
    <el-header>
      <div>
        <span style="margin-left: 30%">Family Tree</span>
        <el-button type="primary" style="margin-left: 20%" @click="jumpBack()">返回</el-button>
        <el-button type="primary" @click="translate()">展示</el-button>
      </div>
    </el-header>
    <el-container>
      <!--<el-aside width="18%">
        <sidebar style="width: 100%"></sidebar>
      </el-aside>-->
      <el-main>
        <el-container>
          <tree-chart :json="treeData"/>
        </el-container>
        <!--<el-button @click="childChange()">Test</el-button>-->
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
    import TreeChart from "vue-tree-chart"

    export default {
        components: {Sidebar, TreeChart},
        component: {sidebar},
        name: 'tree',
        data() {
            return {
                imageUrls: [
                    "http://47.110.134.247/family_members/family_icon0.png",
                    "http://47.110.134.247/family_members/family_icon1.png",
                    "http://47.110.134.247/family_members/family_icon2.png",
                    "http://47.110.134.247/family_members/family_icon3.png",
                    "http://47.110.134.247/family_members/family_icon4.png",
                    "http://47.110.134.247/family_members/family_icon5.png",
                    "http://47.110.134.247/family_members/family_icon6.png",
                    "http://47.110.134.247/family_members/family_icon7.png",
                ],
                myChild: [
                    {
                        name: 'children1',
                        image_url: "http://47.110.134.247/family_members/family_icon0.png",
                    },
                    {
                        name: 'children2',
                        image_url: "http://47.110.134.247/family_members/family_icon5.png",
                        mate: {
                            name: 'mate',
                            image_url: "http://47.110.134.247/family_members/family_icon3.png",
                        },
                        children: [
                            {
                                name: 'grandchild',
                                image_url: "http://47.110.134.247/family_members/family_icon4.png",
                            },
                            {
                                name: 'grandchild2',
                                image_url: "http://47.110.134.247/family_members/family_icon7.png",
                            },
                            {
                                name: 'grandchild3',
                                image_url: "http://47.110.134.247/family_members/family_icon2.png",
                            }
                        ]
                    },
                    {
                        name: 'children3',
                        image_url: "http://47.110.134.247/family_members/family_icon2.png",
                    },
                    {
                        name: 'children4',
                        image_url: "http://47.110.134.247/family_members/family_icon7.png",
                    },

                ],
                inputMethod: false,
                userInput: '',
                balanced: {
                    binarySearchTree: '',
                    balancedBinaryTree: '',
                },
                treeData: {
                    name: 'root',
                    image_url: "http://47.110.134.247/family_members/family_icon7.png",
                    children: [],
                },
                testArr: [4, 2, 1, "#", "#", "#", 6, "#", "#"],
                result: {},
            };
        },
        methods: {
            translate() {
                this.userInput = this.$route.params.userText;
                console.log("转换中........");
                console.log("用户输入:", this.userInput);
                const userInputData = {"user_input": this.userInput};
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/show_tree/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.treeData = res.data;
                }).catch(function (err) {
                    console.log(err);
                });
            },
            changeMethod() {
                this.inputMethod = !this.inputMethod;
            },
            childChange() {
                this.treeData.children = this.myChild;
            },
            jumpBack() {
                this.$router.push({
                    path: '/balanced',
                    name: 'balanced',
                    params: {page: '2-1'},
                });
            },
            /*translate() {
                /!*5,4,3,1,#,2,#,#,#,3,5,2,#,#,#,#,2,#,1,4,#,#,2,#,#*!/
                /!*this.treeData = {
                    'name': '5', 'children': [{
                        'name': '4',
                        'children': [{
                            'name': '3',
                            'children': [{
                                'name': '1',
                                'children': [{
                                    'name': '-inf',
                                    'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                }, {
                                    'name': '2',
                                    'children': [{
                                        'name': '-inf',
                                        'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                    }, {
                                        'name': '-inf',
                                        'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                    }],
                                    'image_url': 'http://47.110.134.247/family_members/family_icon2.png'
                                }],
                                'image_url': 'http://47.110.134.247/family_members/family_icon1.png'
                            }, {'name': '-inf', 'image_url': 'http://47.110.134.247/family_members/family_icon7.png'}],
                            'image_url': 'http://47.110.134.247/family_members/family_icon3.png'
                        }, {
                            'name': '3',
                            'children': [{
                                'name': '5',
                                'children': [{
                                    'name': '2',
                                    'children': [{
                                        'name': '-inf',
                                        'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                    }, {
                                        'name': '-inf',
                                        'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                    }],
                                    'image_url': 'http://47.110.134.247/family_members/family_icon2.png'
                                }, {
                                    'name': '-inf',
                                    'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                }],
                                'image_url': 'http://47.110.134.247/family_members/family_icon5.png'
                            }, {'name': '-inf', 'image_url': 'http://47.110.134.247/family_members/family_icon7.png'}],
                            'image_url': 'http://47.110.134.247/family_members/family_icon3.png'
                        }],
                        'image_url': 'http://47.110.134.247/family_members/family_icon4.png'
                    }, {
                        'name': '2',
                        'children': [{
                            'name': '-inf',
                            'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                        }, {
                            'name': '1',
                            'children': [{
                                'name': '4',
                                'children': [{
                                    'name': '-inf',
                                    'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                }, {
                                    'name': '-inf',
                                    'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                }],
                                'image_url': 'http://47.110.134.247/family_members/family_icon4.png'
                            }, {
                                'name': '2',
                                'children': [{
                                    'name': '-inf',
                                    'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                }, {
                                    'name': '-inf',
                                    'image_url': 'http://47.110.134.247/family_members/family_icon7.png'
                                }],
                                'image_url': 'http://47.110.134.247/family_members/family_icon2.png'
                            }],
                            'image_url': 'http://47.110.134.247/family_members/family_icon1.png'
                        }],
                        'image_url': 'http://47.110.134.247/family_members/family_icon2.png'
                    }], 'image_url': 'http://47.110.134.247/family_members/family_icon5.png'
                }*!/
                console.log(this.treeData)
            }*/
        },
        mounted() {

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
    height: 1600px;
  }

</style>
