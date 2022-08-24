import json
import os
import time

def generate(
        prompt="",
        out="outputs",
        prefix="",
        prompt_dir="",
        n_samples=1
):
    model_path = r"C:\Users\John\Documents\stable-diffusion\models\ldm\stable-diffusion-v1\model.ckpt"
    config = r"C:\Users\John\Documents\stable-diffusion\optimizedSD\v1-inference.yaml"
    os.system(
        r'python C:\Users\John\Documents\stable-diffusion/optimizedSD/optimized_txt2img.py --ckpt "' + model_path + '" --config "' + config + '" --prompt "' + prompt + '" --outdir "' + out + '" --prompt_dir "' + prompt_dir + '" --image_prefix "' + prefix + '" --H 512 --W 512 --seed 27 --n_iter 1 --n_samples "' + str(
            n_samples) + '" --ddim_steps 50')


def generate_from_prompt_file(
        prompt_file,
        out="outputs", # folder containing prompt generation folder
        prefix="",     # file prefixes
        prompt_dir="", # folder for this prompt's images
        n_samples=1
):

    prompts = open(prompt_file,"r").read().splitlines()
    print(prompts)
    if not prompt_dir:
        prompt_dir = prompts[0][:10]

    # TODO - put these in a config file lol
    model_path = r"C:\Users\John\Documents\stable-diffusion\models\ldm\stable-diffusion-v1\model.ckpt"
    config = r"C:\Users\John\Documents\stable-diffusion\optimizedSD\v1-inference.yaml"
    command = fr'''python ../optimizedSD/optimized_txt2img.py 
    --from-file "{prompt_file}" 
    --H 512 
    --W 512 
    --seed 27 
    --n_iter 1 
    --n_samples {len(prompts)} 
    --ddim_steps 50 
    --fixed_seed 
    --prompt_dir "{prompt_dir.replace(" ", "_")}" 
    --ckpt {model_path} 
    --config {config}'''
    os.system(command.replace("\n", " "))
    # TODO - chunk this command so we can run more than 20-ish images
    # TODO - stitch the results into a gif

def generate_prompts(prompt, steps=10, filename = "./gif_prompts.txt"):
    prompts = []
    for i in range(steps):
        prompts.append(prompt.replace('|n|', str(i)))
    open(f"{filename}", "w").write("\n".join(prompts))

def generate_gif(prompt, steps=10):
    generate_prompts(prompt, steps)
    generate_from_prompt_file("./gif_prompts.txt")

# generate_prompts("My name is |n|")

generate_gif("a |n| year old house", 10)