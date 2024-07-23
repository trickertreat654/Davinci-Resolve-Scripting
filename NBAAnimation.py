# Get the Resolve instance
resolve = app.GetResolve()
pm = resolve.GetProjectManager()
project = pm.GetCurrentProject()
mediaPool = project.GetMediaPool()
mediaOut = project.GetRenderFormats()

timeline = project.GetCurrentTimeline()
timelineName = timeline.GetName()
print("Timeline Name: " + timelineName)

fusion = resolve.Fusion()

comp = fusion.GetCurrentComp()
bg = comp.AddTool('Background', 0, 0)

# Set the background color
bg.BackgroundColor = [1, 0.4, 1]  # White background

mrg = comp.AddTool('Merge', 2, 3)
# connect bg to mrg
mrg.ConnectInput('Background', bg)

# Function to create a circle
def create_circle(comp, color, position):
    circle_bg = comp.AddTool('Background')
    circle_bg.BackgroundColor = color
    
    ellipse = comp.AddTool('EllipseMask')
    ellipse.Width = 0.1
    ellipse.Height = 0.1
    ellipse.Center = {0.5, 0.5}  # Center the mask

    # circle_bg.AddMask(ellipse)

    mrg = comp.AddTool('Merge')
    mrg.ConnectInput('Background', bg)
    mrg.ConnectInput('Foreground', circle_bg)
    mrg.Center = position

    return mrg

# Function to create a rectangle
def create_rectangle(comp, color, position):
    rect_bg = comp.AddTool('Background')
    rect_bg.BackgroundColor = color
    
    rect = comp.AddTool('RectangleMask')
    rect.Width = 0.15
    rect.Height = 0.08
    rect.Center = [0.5, 0.5]  # Center the mask

    # rect_bg.AddMask(rect)

    mrg = comp.AddTool('Merge')
    mrg.ConnectInput('Background', bg)
    mrg.ConnectInput('Foreground', rect_bg)
    mrg.Center = position

    return mrg

# Function to add text
def add_text(comp, text_content, position):
    text = comp.AddTool('TextPlus')
    text.StyledText = text_content
    text.Font = "Arial"
    text.Size = 0.04
    text.HorizontalJustification = "Center"
    text.VerticalJustification = "Center"
    text.Center = position

    return text

# Colors for symbols
colors = {
    "MVP": [1, 1, 0.8],       # Light yellow
    "DPOY": [1, 1, 0.6],      # Yellow
    "All NBA 1st": [0.6, 0.6, 0.6],  # Light grey
    "All NBA 2nd": [0.8, 0.8, 0.8],  # Grey
    "All NBA 3rd": [0.4, 0.2, 0.2],  # Dark brown
}

# Positions for symbols
positions = {
    "MVP": [0.1, 0.85],
    "DPOY": [0.1, 0.75],
    "All NBA 1st": [0.1, 0.65],
    "All NBA 2nd": [0.1, 0.55],
    "All NBA 3rd": [0.1, 0.45],
}

# Initialize the merge node
current_merge = mrg

# Add symbols to the composition
for key, color in colors.items():
    if "NBA" in key:
        shape_merge = create_rectangle(comp, color, positions[key])
    else:
        shape_merge = create_circle(comp, color, positions[key])

    # Connect the new shape merge to the current merge
    next_merge = comp.AddTool('Merge')
    next_merge.ConnectInput('Background', current_merge)
    next_merge.ConnectInput('Foreground', shape_merge)
    current_merge = next_merge

# Text labels
labels = {
    "MVP": "MVP",
    "DPOY": "DPOY",
    "All NBA 1st": "All NBA 1st",
    "All NBA 2nd": "All NBA 2nd",
    "All NBA 3rd": "All NBA 3rd",
    "All Defence 1st": "All Defence 1st",
    "All Defence 2nd": "All Defence 2nd",
    "All Star": "All Star",
    "2007-2008": "2007-2008"
}

# Positions for text labels
text_positions = {
    "MVP": [0.25, 0.85],
    "DPOY": [0.25, 0.75],
    "All NBA 1st": [0.25, 0.65],
    "All NBA 2nd": [0.25, 0.55],
    "All NBA 3rd": [0.25, 0.45],
    "All Defence 1st": [0.5, 0.65],
    "All Defence 2nd": [0.5, 0.55],
    "All Star": [0.5, 0.45],
    "2007-2008": [0.5, 0.9]
}

# Add text labels to the composition
for key, label in labels.items():
    text_tool = add_text(comp, label, text_positions[key])
    
    # Connect the new text tool to the current merge
    next_merge = comp.AddTool('Merge')
    next_merge.ConnectInput('Background', current_merge)
    next_merge.ConnectInput('Foreground', text_tool)
    current_merge = next_merge

MediaOut1 = comp.FindTool('MediaOut1')
MediaOut1.ConnectInput('Input', current_merge, 'Output')
