<template>
  <el-container>
    <el-header>密码本</el-header>
    <el-container>
      <el-aside width="210px">
        <sidebar style="width: 209px"></sidebar>
      </el-aside>
      <el-main>
        <!--radio-group begin-->
        <el-row>
          <el-button type="primary" size="small"  @click="showCodeBook('one')">One</el-button>
          <el-button type="success" size="small" @click="showCodeBook('two')">Two</el-button>
          <el-button type="warning" size="small" @click="showCodeBook('three')">Three</el-button>
          <el-button type="danger" size="small" @click="showCodeBook('four')">Four</el-button>
          <!--<el-button type="danger" plain>危险按钮</el-button>-->
        </el-row>
        <!--radio-group end-->
        <!--table begin-->
        <el-table
          :data="tableData"
          border
          style="width: 100%; margin-top: 15px">
          <el-table-column
            prop="id"
            label="序号"
            width="180">
          </el-table-column>
          <el-table-column
            prop="word"
            label="单词"
            width="180">
          </el-table-column>
          <el-table-column
            prop="code"
            label="密码">
          </el-table-column>
        </el-table>
        <!--table end-->

        <!--pagination begin-->
        <div class="block">
          <el-pagination
            @current-change="handleCurrentChange"
            layout="prev, pager, next"
            :total=num>
          </el-pagination>
        </div>
        <!--pagination end-->
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
        name: 'dictionary',
        data() {
            return {
                book: [],
                tableData: [],
                num: 0,
            };
        },
        methods: {
            showCodeBook(dictionaryNumber) {
                console.log("查询........");
                console.log("查询的密码字典为:",dictionaryNumber);
                let chosen = "";
                switch (dictionaryNumber) {
                    case "one":
                        chosen = "00";
                        break;
                    case "two":
                        chosen = "01";
                        break;
                    case "three":
                        chosen = "10";
                        break;
                    case "four":
                        chosen = "11";
                        break;
                    default:
                        break;
                }
                const userInputData = {"user_input": chosen};
                console.log(userInputData)
                axios({
                    method: "post",
                    url: "http://127.0.0.1:8000/cipher/",
                    data: qs.stringify(userInputData),
                }).then((res) => {
                    console.log(res);
                    this.num = res.data.length / 10;
                    this.book = res.data;
                    this.tableData = this.book.slice(0,10);
                    //console.log(this.book);
                });
            },

            handleCurrentChange(val) {
                //该函数再分页按钮改变时触发
                console.log(`当前页: ${val}`);
                let begin = (val - 1) * 10;
                let end = val * 10;
                console.log('begin is: ' + begin + ' ;end is: ' + end);
                this.tableData = this.book.slice(begin,end)
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
</style>
