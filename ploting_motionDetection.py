from videocapture1 import df
import pandas
from bokeh.plotting import output_file,show,figure



p=figure(x_axis_type="datetime",height=500,width=500,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

df['Start'] = pandas.to_datetime(df['Start'])
df['End'] = pandas.to_datetime(df['End'])

q = p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")


output_file("Graph.html")
show(p)

