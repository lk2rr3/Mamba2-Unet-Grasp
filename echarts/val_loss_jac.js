option = {
    title: {
      text: 'Validation Loss vs Epoch on Jacquard V2 Dataset'
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
        data: [0.0289, 0.0262, 0.0254, 0.0248, 0.0245, 0.0240, 0.0240, 0.0233, 0.0239, 0.0239]
      },
      {
        name: 'small',
        type: 'line',
        data: [0.0285, 0.0259, 0.0250, 0.0245, 0.0234, 0.0233, 0.0240, 0.0229, 0.0243, 0.0228]
      },
      {
        name: 'base',
        type: 'line',
        data: [0.0271, 0.0262, 0.0253, 0.0252, 0.0241, 0.0234, 0.0237, 0.0229, 0.0232, 0.0223]
      },
      {
        name: 'large',
        type: 'line',
        data: [0.0271, 0.0268, 0.0250, 0.0240, 0.0241, 0.0243, 0.0238, 0.0245, 0.0238, 0.0252]
      },
      {
        name: 'GR-ConvNet',
        type: 'line',
        data: [0.0413, 0.0361, 0.0323, 0.0305, 0.0279, 0.0268, 0.0260, 0.0256, 0.0263, 0.0258]
      },
      {
        name: 'TF-Grasp',
        type: 'line',
        data: [0.0930, 0.0829, 0.0820, 0.0801, 0.0782, 0.0772, 0.0825, 0.0798, 0.0766, 0.0751]
      }
    ]
  };