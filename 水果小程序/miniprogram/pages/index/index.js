//index.js
const app = getApp()

Page({
  data: {
    jiluShow:false,
    youhuijuanShow: false,
    xiaofeijilu:[
      {
        name:'洪合店',
        date:'18.10.12 15:24',
        money:'27.5',
        content:[
          {shuiguoming:'苹果',zhongliang:'2',money:'18'},
          { shuiguoming: '香蕉', zhongliang: '1.5', money: '9.5' },
        ]
      },
      {
        name: '新美村店',
        date: '18.10.15 17:06',
        money: '560.5',
        content: [
          { shuiguoming: '柚子', zhongliang: '3.5', money: '28' },
          { shuiguoming: '橘子', zhongliang: '11.5', money: '6' },
          { shuiguoming: '西瓜', zhongliang: '4', money: '12' },
          { shuiguoming: '苹果', zhongliang: '1', money: '124' },
        ]
      },
      {
        name: '濮院店',
        date: '18.10.22 14:22',
        money: '26',
        content: [
          { shuiguoming: '西瓜', zhongliang: '5', money: '18' },
          { shuiguoming: '橘子', zhongliang: '2', money: '8' },
        ]
      },
      {
        name: '泰石店',
        date: '18.10.20 16:52',
        money: '45',
        content: [
          { shuiguoming: '橘子', zhongliang: '3', money: '12' },
          { shuiguoming: '柿子', zhongliang: '2.5', money: '15' },
          { shuiguoming: '西瓜', zhongliang: '4.5', money: '18' },
        ]
      },
    ],
    youhuijuan:[
      {tiaojian:'满88元可用',shuoming:'全店通用满立减',jine:'5',youxiaoqi:'10.15~12.31'},
      {tiaojian:'满100元可用',shuoming:'全店通用满立减',jine:'10',youxiaoqi:'10.15~12.31'},
      { tiaojian: '满200元可用', shuoming: '全店通用满立减', jine: '20', youxiaoqi: '10.15~12.31' },
    ]
  },
  jiluClick(){
    this.setData({ jiluShow: !this.data.jiluShow});
  },
  youhuijuan() {
    this.setData({ youhuijuanShow: !this.data.youhuijuanShow });
  },


})
