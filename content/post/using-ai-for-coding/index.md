---
title: "Is AI ready to do my coding for me?"
subtitle: "No. But it definitely has it's uses!"
tags: ["Technical", "Python", "Programming", "AI"]
date: 2024-12-10
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Has AI defeated the programmer?"
  focal_point: "Centre"
  placement: 3
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["instagram-story-cutter"]
---

So during my most recent project, I was struggling to figure out how to use a specific python module. It wasn't well documented and the discussion threads on the project gave hints but the answers weren't specific enough or complete enough. I even tried doing what no developer likes doing, posting a question on the community help themselves!!! I was getting frustrated and almost gave up, falling back to an inferior module. Then I realised what I really needed was another opinion, someone to bounce ideas off of and question with ideas. AI could be my friend.

## How I used AI

I had three uses of AI, prompts with LLM AI models, AI based code autocomplete and logo creation for my project.

### Prompt based help

This was my most used form of AI. The ability to send a prompt of some type and then an LLM model attempted to answer the prompt. This effectively functioned as a conversational assistant. It felt natural and took up a low cognitive load when I was trying to solve problems that required significant concentration. The two models I used were Claude's Sonnet 3.5 model (Haiku) and ChatGPT 4o Mini, which had there own pros and cons.

#### Claude Sonnet vs OpenAI ChatGPT

I had heard that Claude's latest Sonnet model was the best performing model for coding problems so I was drawn to try this despite my experience of having used ChatGPT in the past (admittedly for non-coding prompts). So I decided to test both of them and see which one gave me the best results. My prompt was identical and relatively simple for each test:

`how would I use the trim filter from ffmpeg using the pyav python package?`

<details>
<summary>Claude's Initial Response - Click to reveal</summary>

```python
  import av

  def trim_video(input_file, output_file, start_time, end_time):
      """
      Trim a video file using PyAV

      Args:
          input_file (str): Path to the input video file
          output_file (str): Path to save the trimmed video
          start_time (float): Start time of the trim in seconds
          end_time (float): End time of the trim in seconds
      """
      # Open the input container
      with av.open(input_file) as input_container:
          # Create an output container
          with av.open(output_file, 'w') as output_container:
              # Copy the video stream
              video_stream = input_container.streams.video[0]
              output_video_stream = output_container.add_stream(
                  template=video_stream
              )

              # Copy the audio stream (optional)
              if input_container.streams.audio:
                  audio_stream = input_container.streams.audio[0]
                  output_audio_stream = output_container.add_stream(
                      template=audio_stream
                  )

              # Seek to the start time
              input_container.seek(start_time)

              # Process frames
              for packet in input_container.demux():
                  # Check if we've passed the end time
                  if packet.pts * packet.time_base > end_time:
                      break

                  # Decode and encode video frames
                  if packet.stream.type == 'video':
                      for frame in packet.decode():
                          # Only process frames within the trim range
                          if start_time <= frame.pts * video_stream.time_base <= end_time:
                              for encoded_packet in output_video_stream.encode(frame):
                                  output_container.mux(encoded_packet)

                  # Process audio frames similarly (optional)
                  elif packet.stream.type == 'audio':
                      for frame in packet.decode():
                          if start_time <= frame.pts * audio_stream.time_base <= end_time:
                              for encoded_packet in output_audio_stream.encode(frame):
                                  output_container.mux(encoded_packet)

              # Flush any remaining frames
              output_video_stream.close()
              if input_container.streams.audio:
                  output_audio_stream.close()
  # Example usage
  if __name__ == "__main__":
      trim_video(
          input_file='input_video.mp4', 
          output_file='trimmed_video.mp4', 
          start_time=10.0,  # Start at 10 seconds 
          end_time=30.5     # End at 30.5 seconds
      )
```

</details>

<details>
<summary>ChatGPT's Initial Response - Click to reveal</summary>

```python
import av

# Input and output file paths
input_file = 'input.mp4'
output_file = 'output.mp4'

# Open the input file
input_container = av.open(input_file)

# Open the output container
output_container = av.open(output_file, mode='w')

# Select the video stream
video_stream = input_container.streams.video[0]

# Add a new video stream to the output
output_stream = output_container.add_stream(template=video_stream)

# Define trim start and end times in seconds
start_time = 5.0  # Start at 5 seconds
end_time = 10.0   # End at 10 seconds

# Start processing packets
for packet in input_container.demux(video_stream):
    for frame in packet.decode():
        # Check if the frame is within the trim range
        if frame.pts is not None:
            time_in_seconds = frame.pts * frame.time_base
            if start_time <= time_in_seconds < end_time:
                # Re-encode and write the frame
                packet = output_stream.encode(frame)
                if packet:
                    output_container.mux(packet)

# Finalize encoding
output_container.mux(output_stream.encode(None))

# Close the containers
input_container.close()
output_container.close()
```

</details>

Claude's code is better structured and it uses the `with` statement, so it handles files more safely. This put Claude ahead initially but actually neither of the models had done what I had asked, which was to use the `Trim` filter. So I prompted with the following:

`I thought you could use ffmpeg filters using the graph class in Pyav. Is that not the case?`

And these were the responses:

<details>
<summary>Claude's Second Response - Click to reveal</summary>

```python
import av

def trim_video_with_filter(input_file, output_file, start_time, duration):
    """
    Trim a video using PyAV FilterGraph
    
    Args:
        input_file (str): Path to the input video file
        output_file (str): Path to save the trimmed video
        start_time (float): Start time of the trim in seconds
        duration (float): Duration of the trimmed segment in seconds
    """
    # Create a filter graph
    graph = av.FilterGraph()
    
    # Create input and output contexts
    with av.open(input_file) as input_container:
        # Get the first video stream
        input_stream = input_container.streams.video[0]
        
        # Create input filter
        input_filter = graph.add_input(input_stream)
        
        # Apply trim filter
        trim_filter = input_filter.trim(start=start_time, duration=duration)
        
        # Optionally add scale or other filters here
        # For example: scaled_filter = trim_filter.scale(width=1280, height=720)
        
        # Create output
        output_filter = trim_filter.output('output')
        
        # Open output file
        with av.open(output_file, 'w') as output_container:
            # Add output stream
            output_stream = output_container.add_stream(
                template=input_stream
            )
            
            # Link the filter graph to the output stream
            output_filter.link_to(output_stream)
            
            # Process the filter graph
            for packet in graph.run():
                output_container.mux(packet)

# Example usage
if __name__ == "__main__":
    trim_video_with_filter(
        input_file='input_video.mp4', 
        output_file='trimmed_video.mp4', 
        start_time=10.0,  # Start at 10 seconds 
        duration=20.5     # Trim for 20.5 seconds
    )

# More advanced example with multiple filters
def advanced_video_processing(input_file, output_file):
    """
    Demonstrate chaining multiple FFmpeg filters
    """
    graph = av.FilterGraph()
    
    with av.open(input_file) as input_container:
        input_stream = input_container.streams.video[0]
        
        # Create input filter
        input_filter = graph.add_input(input_stream)
        
        # Chain multiple filters
        trimmed = input_filter.trim(start=5, duration=30)
        scaled = trimmed.scale(width=1280, height=720)
        color_adjusted = scaled.eq(brightness=0.1, contrast=1.2)
        
        # Create output
        output_filter = color_adjusted.output('output')
        
        with av.open(output_file, 'w') as output_container:
            output_stream = output_container.add_stream(template=input_stream)
            output_filter.link_to(output_stream)
            
            for packet in graph.run():
                output_container.mux(packet)

# Demonstrate filter options
def show_filter_options():
    """
    Example of various filter options available
    """
    # Note: These are conceptual examples to show filter possibilities
    graph = av.FilterGraph()
    input_filter = graph.add_input(None)  # Placeholder
    
    # Some filter examples
    input_filter.trim(start=5)  # Trim from 5 seconds
    input_filter.scale(width=1280, height=720)  # Resize
    input_filter.eq(brightness=0.1, contrast=1.2)  # Color adjustment
    input_filter.rotate(angle=90)  # Rotate video
    input_filter.crop(width=640, height=480)  # Crop video
```

</details>

<details>
<summary>ChatGPT's Second Response - Click to reveal</summary>

```python
import av

# Input and output file paths
input_file = 'input.mp4'
output_file = 'output_trimmed.mp4'

# Open the input file
input_container = av.open(input_file)

# Get the video stream from the input
video_stream = input_container.streams.video[0]

# Open the output container
output_container = av.open(output_file, mode='w')
output_stream = output_container.add_stream(template=video_stream)

# Create a filter graph
filter_graph = av.filter.Graph()

# Add the video stream as a source
source = filter_graph.add_buffer(template=video_stream)

# Add the trim filter
start_time = 5.0  # in seconds
end_time = 10.0  # in seconds
trim = filter_graph.add("trim", start=start_time, end=end_time)

# Link the source to the trim filter
source.link_to(trim)

# Add a sink to the graph
sink = filter_graph.add("buffersink")
trim.link_to(sink)

# Configure the filter graph
filter_graph.configure()

# Decode, filter, and encode frames
for packet in input_container.demux(video_stream):
    for frame in packet.decode():
        # Push the frame into the filter graph
        filter_graph.push(frame)

        # Pull frames from the filter graph after processing
        while True:
            filtered_frame = filter_graph.pull()
            if filtered_frame is None:
                break

            # Re-encode the filtered frame and write it to the output
            packet = output_stream.encode(filtered_frame)
            if packet:
                output_container.mux(packet)

# Flush the encoder
output_container.mux(output_stream.encode(None))

# Close the input and output containers
input_container.close()
output_container.close()
```

</details>

Now at first glance it does look like Claude has won here, however I knew from my previous googling of filters and how they worked in PyAV, that Claude had actually juist made up a bunch of functions and put them together. Now admittedly it looks clean and I kind of wish that the implementation did look more like what Claude had thought, but it isn't. ChatGPT's code was still structured worse and didn't use the `with` statement, but at least it actually used the module how you are supposed to use it. I have also found out that there is a Python specific model based on the ChatGPT 4o model, and that appears to give better quality code.

So my conclusion is that ChatGPT wins in this scenario, but it's worth trying out both models and then go with the one which gives better responses after a couple prompts. One of the real advantages of either of these models was that it got the code off the ground and then I could tinker with it. Neither of them actually even ran without an exception when I copied them but it made getting started so much easier; removing the boilerplate and setup time for creating a new project. I will definitely being using them going forward to make me more productive.

### Code autocomplete - Intellicode VSCode Extension

This is pretty self-explanatory but whilst I was looking at AI use cases for development I thought that I would check if there were any extensions for my IDE that would be useful. The Intellicode extension had a high rating and many downloads so I installed it and here are my thoughts.

In short Intellicode is ok. Intellicode uses `Tab` to fill in the autocomplete so I found that it would sometimes give suggestions, when I just wanted to add a tab spacing in my code. Particularly annoying for Python development. And sometimes the suggestions weren't of any value.

{{<figure src="AI-WHY.png" caption="This is both not what I want and is preventing me from adding tabs">}}

Other times it did give better suggestions. On the whole it's not worth installing but may be worth trying at a later date.

### Image Generation - Creating a logo

As someone with the artistic ability of a stone I was glad to see that there was an image generation model specifically for creating logos. I thought it would be nice to have one just to show off and use when I turn the instagram story cutter into a website. It started off so well, with something that looked like it could be a logo. Possibly because it was a bit too close to Instagrams own logo.

{{<figure src="first-logo.png" caption="A bit close to the instagram logo">}}

I then prompted for something that emphasized that multiple clips were being created:

{{<figure src="second-logo.png" caption="Somewhat cursed generation">}}

I liked the video player in the bottom right so tried to prompt for that and then DALL.E forgot the logo brief:

{{<figure src="third-logo.png" caption="It looks nice but isn't a logo">}}

Then my final attempt but it still kept it 3D despite asking for a view looking from above so that it didn't have any depth to it:

{{<figure src="last-logo.png" caption="Close enough">}}

So was this useful. Yes! Although I won't be using any of the images generated it gave me some really good ideas and it worked out a colour pallete that I liked. For someone who always struggles with starting from scratch on creative endeavours this is a great tool to give me ideas and direction.

## Overall thoughts

My journey into the world of AI for productivity was a fun one. It clearly is not at the point where it can do all the work and although I am impressed by it's speed to generate an answer, it's clear that these models don't have true intelligence. They don't generate based on a logic but purely based on probability. This does make for some very good ideas though and it genuinely made me consider my approach to different problems. But am I afraid of it taking my job? Not really!
