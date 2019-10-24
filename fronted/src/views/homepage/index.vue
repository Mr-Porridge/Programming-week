<template>
  <el-container>
    <el-header>B17040425 周奕飞 题目 A6 B6 </el-header>
    <el-container>
      <el-aside width="210px">
      </el-aside>
      <el-main>
        <el-container>
          <el-button type="primary" @click="explore()">Explore!</el-button>
        </el-container>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
    export default {
        name: 'homepage',
        data() {
            return {};
        },
        methods: {
            explore() {
                this.$router.push({
                    path: '/balanced',
                    name: 'balanced',
                    params: {},
                })
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
    height: 550px;
  }

  .checking {
    width: 500px;
    height: 60px;
  }
</style>
