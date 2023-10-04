import matplotlib
matplotlib.use('Agg')  # Usar el backend 'Agg' (que no requiere una GUI)


import charts

def run():
    charts.generate_pie_chart()
    
if __name__ == "__main__":
    run()
    
print("v")