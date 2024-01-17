import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

def fetch_and_parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('div', {'class': 'document', 'role': 'main'})

def convert_to_latin1(text):
    # Replace non-Latin1 characters
    return text.encode('latin-1', 'replace').decode('latin-1')

def urls_to_pdf(urls, pdf_filename):
    pdf = FPDF()
    pdf.set_font("Arial", size = 12)
    
    for url in urls:
        pdf.add_page()
        content = fetch_and_parse("https://docs.flame-engine.org/1.14.0/"+url)
        if content:
            for element in content.stripped_strings:
                encoded_text = convert_to_latin1(element)
                pdf.cell(0, 10, encoded_text, ln=True)
    
    pdf.output(pdf_filename)

# List of URLs to process
urls = ["other_modules/jenny/runtime/dialogue_line.html", "bridge_packages/flame_fire_atlas/fire_atlas.html", "#outside-of-the-scope-of-the-engine", "tutorials/platformer/step_2.html", "flame/overlays.html", "flame/other/debug.html", "flame/rendering/palette.html", "flame/rendering/images.html", "other_modules/jenny/language/expressions/expressions.html", "bridge_packages/flame_lottie/flame_lottie.html", "tutorials/space_shooter/space_shooter.html", "flame/effects.html", "tutorials/space_shooter/step_2.html", "flame/inputs/gesture_input.html", "other_modules/jenny/language/commands/local.html", "other_modules/jenny/runtime/node.html", "tutorials/klondike/step3.html", "other_modules/jenny/runtime/character_storage.html", "flame/platforms.html", "other_modules/jenny/language/markup.html", "other_modules/jenny/language/commands/wait.html", "other_modules/jenny/language/commands/jump.html", "flame/inputs/inputs.html", "tutorials/space_shooter/step_5.html", "other_modules/jenny/runtime/command_storage.html", "tutorials/platformer/platformer.html", "bridge_packages/flame_rive/flame_rive.html", "tutorials/platformer/step_6.html", "other_modules/jenny/language/expressions/operators.html", "other_modules/jenny/runtime/jenny_runtime.html", "development/style_guide.html", "flame/inputs/hardware_keyboard_detector.html", "other_modules/jenny/language/expressions/functions/random.html", "bridge_packages/flame_isolate/isolate.html", "other_modules/other_modules.html", "other_modules/jenny/runtime/yarn_project.html", "flame/game_widget.html", "other_modules/jenny/runtime/character.html", "#multiplayer-netcode", "flame/layout/align_component.html", "other_modules/jenny/jenny.html", "bridge_packages/flame_bloc/bloc_components.html", "flame/camera_component.html", "other_modules/jenny/language/commands/stop.html", "bridge_packages/flame_bloc/bloc.html", "other_modules/jenny/runtime/dialogue_option.html", "other_modules/jenny/runtime/dialogue_runner.html", "other_modules/jenny/language/commands/character.html", "development/contributing.html", "bridge_packages/flame_tiled/flame_tiled.html", "bridge_packages/flame_isolate/flame_isolate.html", "flame/rendering/particles.html", "#id1", "/", "development/documentation.html", "flame/components.html", "tutorials/klondike/step2.html", "bridge_packages/flame_audio/bgm.html", "other_modules/oxygen/components.html", "other_modules/jenny/language/expressions/functions/misc.html", "bridge_packages/flame_svg/flame_svg.html", "other_modules/jenny/runtime/dialogue_view.html", "bridge_packages/flame_forge2d/joints.html", "flame/collision_detection.html", "other_modules/jenny/language/commands/user_defined_commands.html", "other_modules/jenny/language/nodes.html", "tutorials/platformer/step_7.html", "bridge_packages/flame_audio/audio.html", "tutorials/klondike/step5.html", "#installation", "#", "flame/inputs/keyboard_input.html", "other_modules/jenny/runtime/dialogue_choice.html", "flame/inputs/pointer_events.html", "tutorials/klondike/klondike.html", "flame/rendering/decorators.html", "#getting-started", "bridge_packages/flame_audio/audio_pool.html", "flame/structure.html", "other_modules/jenny/language/commands/set.html", "bridge_packages/flame_forge2d/flame_forge2d.html", "tutorials/space_shooter/step_3.html", "bridge_packages/flame_spine/flame_spine.html", "tutorials/space_shooter/step_4.html", "bridge_packages/flame_network_assets/flame_network_assets.html", "flame/inputs/drag_events.html", "other_modules/jenny/language/commands/if.html", "other_modules/jenny/runtime/variable_storage.html", "flame/rendering/layers.html", "other_modules/jenny/language/expressions/functions/numeric.html", "tutorials/bare_flame_game.html", "development/development.html", "bridge_packages/flame_splash_screen/flame_splash_screen.html", "bridge_packages/flame_oxygen/flame_oxygen.html", "other_modules/jenny/language/commands/commands.html", "other_modules/oxygen/oxygen.html", "tutorials/platformer/step_5.html", "other_modules/jenny/runtime/markup_attribute.html", "flame/rendering/rendering.html", "other_modules/jenny/runtime/function_storage.html", "resources/resources.html", "flame/other/other.html", "tutorials/space_shooter/step_1.html", "other_modules/jenny/runtime/user_defined_command.html", "tutorials/platformer/step_4.html", "bridge_packages/flame_riverpod/widget.html", "flame/inputs/other_inputs.html", "#about-flame", "flame/inputs/tap_events.html", "bridge_packages/flame_forge2d/forge2d.html", "tutorials/klondike/step1.html", "bridge_packages/flame_fire_atlas/flame_fire_atlas.html", "bridge_packages/flame_audio/flame_audio.html", "other_modules/jenny/language/language.html", "bridge_packages/flame_tiled/layers.html", "bridge_packages/flame_bloc/flame_bloc.html", "bridge_packages/flame_riverpod/flame_riverpod.html", "flame/flame.html", "other_modules/jenny/language/options.html", "bridge_packages/flame_riverpod/component.html", "bridge_packages/bridge_packages.html", "other_modules/jenny/language/expressions/functions/type.html", "flame/layout/layout.html", "tutorials/platformer/step_1.html", "flame/rendering/text_rendering.html", "other_modules/jenny/language/lines.html", "flame/game.html", "tutorials/platformer/step_3.html", "flame/router.html", "flame/other/util.html", "tutorials/klondike/step4.html", "bridge_packages/flame_tiled/tiled.html", "development/testing_guide.html", "other_modules/jenny/language/commands/declare.html", "other_modules/jenny/language/expressions/functions/functions.html", "tutorials/space_shooter/step_6.html", "bridge_packages/flame_riverpod/riverpod.html", "other_modules/jenny/language/expressions/variables.html", "other_modules/jenny/language/commands/visit.html", "flame/other/widgets.html", "tutorials/tutorials.html", "bridge_packages/flame_svg/svg.html", "bridge_packages/flame_rive/rive.html"] # Replace with your URLs

# Name of the output PDF file
pdf_filename = 'output.pdf'

# Generate the PDF
urls_to_pdf(urls, pdf_filename)
