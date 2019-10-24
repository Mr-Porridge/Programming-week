const Mock = require('mockjs');
import qs from 'qs'
const tree =
  {
    "status": 0,
    "message": "成功",
    "data": {
      "exist": 1 //0：不存在 ，1：存在
    }
  };

Mock.mock('http://balancedtree.com', tree);
