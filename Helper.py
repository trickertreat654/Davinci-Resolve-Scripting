def create_text(comp = None, message = "Hello World", position = [0.5,0.5], size = 0.1, input = None, output = None, nodeX = 0): 
    text = comp.AddTool('TextPlus', nodeX, 2)
    mrg = comp.AddTool('Merge', nodeX, 0)
    mrg.Center = position
    mrg.ConnectInput('Foreground', text)
    
    mrg.ConnectInput('Background', input)
    # input.ConnectInput('Input', None)

    output.ConnectInput('Background', None)
    output.ConnectInput('Background', mrg, 'Output')
   
    text.StyledText = message
    text.Size = size
    text.Position = position
   
    return mrg

def merge_tool(comp = None, input = None, output = None, nodeX = 0):
    mrg = comp.AddTool('Merge', nodeX, 0)
    mrg.ConnectInput('Background', input)
    output.ConnectInput('Background', None)
    output.ConnectInput('Background', mrg, 'Output')
    return mrg
