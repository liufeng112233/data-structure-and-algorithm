import paddlehub as hub
module = hub.Module(name="ernie_vilg")
results = module.generate_image(text_prompts=["巨大的白色城堡"])