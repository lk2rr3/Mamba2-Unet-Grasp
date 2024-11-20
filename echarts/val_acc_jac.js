option = {
    title: {
      text: 'Validation Accuracy vs Epoch on Jacquard V2 Dataset'
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
        data: [0.799070, 0.808952, 0.857392, 0.867661, 0.886844, 0.906026, 0.908351, 0.882968, 0.900019, 0.880643]
      },
      {
        name: 'small',
        type: 'line',
        data: [0.722534, 0.849448, 0.895563, 0.898663, 0.906995, 0.902926, 0.887812, 0.918233, 0.912033, 0.904088]
      },
      {
        name: 'base',
        type: 'line',
        data: [0.863399, 0.900213, 0.869211, 0.892850, 0.912808, 0.915520, 0.896725, 0.910676, 0.917845, 0.933734]
      },
      {
        name: 'large',
        type: 'line',
        data: [0.878124, 0.855648, 0.879287, 0.907576, 0.888200, 0.899826, 0.899438, 0.917652, 0.891300, 0.892075]
      },
      {
        name: 'GR-ConvNet',
        type: 'line',
        data: [0.637473, 0.729316, 0.778919, 0.784150, 0.852742, 0.866111, 0.868243, 0.875993, 0.846541, 0.844410]
      },
      {
        name: 'TF-Grasp',
        type: 'line',
        data: [0.400116, 0.591358, 0.618097, 0.600465, 0.548731, 0.644449, 0.611316, 0.639217, 0.651424, 0.664794]
      }
    ]
  };