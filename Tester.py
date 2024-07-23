import Helper
import Awards  

# Get the Resolve instance
resolve = app.GetResolve()
pm = resolve.GetProjectManager()
project = pm.GetCurrentProject()
mediaPool = project.GetMediaPool()
# get media out
mediaOut = project.GetRenderFormats()
timeline = project.GetCurrentTimeline()
timelineName = timeline.GetName()
print("Timeline Name: " + timelineName)
fusion = resolve.Fusion()
comp = fusion.GetCurrentComp()





MediaOut1 = comp.AddTool('MediaOut',6,0)
bg = comp.AddTool('Background', 0, 0)
bg.TopLeftRed = 0.5
MainMerge = comp.AddTool('Merge', 5, 0)
MainMerge.ConnectInput('Background', bg)
MediaOut1.ConnectInput('Input', MainMerge, 'Output')
mrg1 = Helper.create_text(comp, "2007-2008", [0.5,0.8],0.1, bg, MainMerge, 2)
mrg2 = Helper.create_text(comp, "MVP", [0.15,0.7],0.08, mrg1, MainMerge, 4)


shape = comp.AddTool('sStar', 0, -3)
render = comp.AddTool('sRender', 1, -3)
transform = comp.AddTool('Transform', 2, -3)
render.ConnectInput('Input', shape, 'Output')
transform.ConnectInput('Input', render, 'Output')
mrg3 = Helper.merge_tool(comp, mrg1, mrg2, 3)
mrg3.ConnectInput('Foreground', transform)

# Awards
award = Awards.Awards("MVP")

print(award.name)

