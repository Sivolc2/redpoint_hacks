import replicate
import webbrowser

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")
output_url = version.predict(prompt="electric sheep, neon, synthwave")[0]
print(output_url)
webbrowser.open(output_url)
