option = {
  title: {
    text: 'Validation Accuracy vs Epoch on Cornell Dataset'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['tiny', 'small', 'base', 'large', 'GR-ConvNet', 'TF-Grasp']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: [0,1,2,3,4,5,6,7,8,9]
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: 'tiny',
      type: 'line',
      data: [0.887640, 0.898876, 0.943820, 0.921348, 0.898876, 0.955056, 0.921348, 0.932584, 0.865169, 0.955056]
    },
    {
      name: 'small',
      type: 'line',
      data: [0.820225, 0.921348, 0.977528, 0.966292, 0.876404, 0.943820, 0.910112, 0.910112, 0.977528, 0.955056]
    },
    {
      name: 'base',
      type: 'line',
      data: [0.865169, 0.876404, 0.831461, 0.898876, 0.876404, 0.932584, 0.921348, 0.887640, 0.898876, 0.932584]
    },
    {
      name: 'large',
      type: 'line',
      data: [0.921348, 0.910112, 0.910112, 0.943820, 0.898876, 0.966292, 0.898876, 0.921348, 0.932584, 0.955056]
    },
    {
      name: 'GR-ConvNet',
      type: 'line',
      data: [0.528090, 0.741573, 0.730337, 0.775281, 0.898876, 0.887640, 0.764045, 0.865169, 0.865169, 0.943820]
    },
    {
      name: 'TF-Grasp',
      type: 'line',
      data: [0.561798, 0.325843, 0.426966, 0.573034, 0.752809, 0.741573, 0.606742, 0.696629, 0.651685, 0.662921]
    }
  ]
};