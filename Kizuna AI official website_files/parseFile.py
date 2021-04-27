import shutil, os, re


if not os.path.isdir('kizunaai'):
    os.mkdir('kizunaai')

for i in os.listdir('.'):
    if not i == 'parseFile.py' and not i == 'kizunaai':
        if re.search('\.下載', i):
            shutil.move(
                i,
                os.path.join('kizunaai', re.sub('\.下載', '', i))
            )
        else:
            shutil.move(
                i,
                os.path.join('kizunaai', i)
            )

with open('kizunaai/index.html', 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html><html><head><script type="text/javascript" src="./jquery.js"></script><script type="text/javascript" src="./ScrollMagic.min.js"></script> <script type="text/javascript" src="./ytmovie.js"></script><!-- three.js --><script type="text/javascript" src="./MotionSensor.js"></script><script type="text/javascript" src="./three.js"></script><script type="module" src="./three.module.js"></script><script type="text/javascript" src="./Tween.js"></script><script type="text/javascript" src="./TGALoader.js"></script><script type="text/javascript" src="./mmdparser.js"></script><script type="text/javascript" src="./MMDLoader.js"></script><script type="text/javascript" src="./ammo.js"></script><script type="text/javascript" src="./CCDIKSolver.js"></script><script type="text/javascript" src="./MMDPhysics.js"></script><script type="text/javascript" src="./MMDAnimationHelper.js"></script><script src="animation.js"></script></head><body><div id="mycanvas"></div></body></html>')