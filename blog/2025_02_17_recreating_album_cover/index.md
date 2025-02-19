# Recreating Album Cover

<p align="center">
<img src="examples/Kendrick Lamar_DAMN..jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/Kendrick Lamar_DAMN._generated.jpg" width="47%" style="padding: 1% 1% 1% 1%">
</p>

I wanted to test out LLMs to generate prompts for text-to-image models to recreate album cover art with me in it.

I used [piebro/spotify-statistics](https://github.com/piebro/spotify-statistics/) to get the album covers of my favorite albums.
But it's also possible to just manually download selected album covers.
I filtered the covers for the ones that have a person and that I thought would be fun to recreate.

With a little script I automated the process of generating the prompts for all selected albums using this prompt and system prompt with claude 3.5:

<details>
<summary>Prompt and System Prompt</summary>

```md

## Prompt

Analyze this image and create a text-to-image prompt with the following structure:

1. Technical Foundation:
- Image quality and camera specifications
- Lighting setup and effects
- Composition and framing
- Post-processing or special effects

2. Subject Description:
For the main subject, mark with {person} and describe ONLY:
- Pose and positioning
- Expression and gaze
- Hand positions and gestures
- Basic composition in frame

3. Environment & Style:
- Background details
- Props and supporting elements
- Overall artistic style
- Specific artist/photographer references

4. Clothing & Accessories:
- Detailed description of garments
- Cultural elements and patterns
- Colors and textures
- Any text or symbolic elements

Format as a single, flowing paragraph optimized for text-to-image generation. Focus on technical precision while maintaining natural language flow. If there is not person in the image, return only 'Nothing to substitute' and dont write a prompt.

## System Prompt

You are a professional prompt engineer specializing in text-to-image systems. Your expertise includes:
1. Creating precise, technical descriptions that translate visual elements into text
2. Understanding how to separate subject descriptions for LoRA substitution
3. Maintaining artistic intent and cultural elements while allowing for style transfer
4. Structuring prompts to work effectively with modern AI image generation systems

When crafting prompts, you:
- Separate technical elements (lighting, composition, quality) from subject descriptions
- Use specific photography/art direction terminology
- Include style references that help maintain the intended aesthetic
- Structure descriptions to work with LoRA substitutions while preserving artistic intent
- Describe all text on the image and the style of the text

You provide only the prompt text, with no explanations or commentary. If there is not person in the image, return only 'Nothing to substitute' and dont write a prompt.
```

</details>

The generated prompt for the first example looks like this:

```
High-resolution album cover photo, shot with professional DSLR camera, dramatic side lighting creating shadows on brick wall, cinematic color grading with deep reds and muted tones, sharp focus, 8K quality. {person} sitting in contemplative downward gaze, head tilted slightly forward, shoulders relaxed, intimate close-up portrait composition from chest up, positioned slightly off-center. Weathered red brick wall background with textural detail, urban documentary style photography reminiscent of street portraiture. Plain white crew neck t-shirt with relaxed fit, parental advisory explicit content label in bottom right corner, large red "DAMN." text overlaid in serif font at top of image. Post-processing emphasizes contrast and shadow detail, slight film grain texture, high dynamic range maintaining detail in both highlights and shadows.
```

I used FLUX.1 [dev] with a LORA trained on image of me.
In the prompt I replaced `{person}` with the trigger word for the LORA.
This prompt worked quite well even showing the parental advisory label.
Some images worked better than others and for some I generated multiple images to get a good one, but overall it worked surprisingly well and I'm happy with the results.

<p align="center">
<img src="examples/Oliver Tree_Alien Boy EP.jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/Oliver Tree_Alien Boy EP_generated.jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/Masayoshi Takanaka_スーパー・セレクション.jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/Masayoshi Takanaka_スーパー・セレクション_generated.jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/Various Artists_Call Me By Your Name (Original Motion Picture Soundtrack).jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/Various Artists_Call Me By Your Name (Original Motion Picture Soundtrack)_generated.jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/BROCKHAMPTON_SATURATION II.jpg" width="47%" style="padding: 1% 1% 1% 1%">
<img src="examples/BROCKHAMPTON_SATURATION II_generated.jpg" width="47%" style="padding: 1% 1% 1% 1%">
</p>









