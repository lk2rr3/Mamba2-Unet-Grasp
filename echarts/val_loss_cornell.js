option = {
    title: {
      text: 'Validation Loss vs Epoch on Cornell Dataset'
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
        data: [0.0848, 0.0691, 0.0669, 0.0630, 0.0751, 0.0628, 0.0540, 0.0642, 0.0700, 0.0673]
      },
      {
        name: 'small',
        type: 'line',
        data: [0.0668, 0.0572, 0.0734, 0.0730, 0.0665, 0.0674, 0.0693, 0.0691, 0.0674, 0.0550]
      },
      {
        name: 'base',
        type: 'line',
        data: [0.0834, 0.0673, 0.0784, 0.0706, 0.0606, 0.0640, 0.0687, 0.0577, 0.0548, 0.0622]
      },
      {
        name: 'large',
        type: 'line',
        data: [0.0593, 0.0655, 0.0602, 0.0731, 0.0830, 0.0627, 0.0633, 0.0815, 0.0508, 0.0649]
      },
      {
        name: 'GR-ConvNet',
        type: 'line',
        data: [0.0817, 0.0800, 0.0815, 0.0806, 0.0695, 0.0715, 0.0755, 0.0629, 0.0689, 0.0702]
      },
      {
        name: 'TF-Grasp',
        type: 'line',
        data: [0.1853, 0.2355, 0.2010, 0.1818, 0.1502, 0.1743, 0.1768, 0.1559, 0.1456, 0.1925]
      }
    ]
  };