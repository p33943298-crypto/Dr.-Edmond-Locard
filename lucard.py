from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- RECOMENDACIÓN: Manejadores de Excepciones HTTP (404 y 500) ---
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc):
    if request.url.path.startswith("/api/"):
        return JSONResponse(status_code=404, content={"error": "Resource not found"})
    return HTMLResponse(content="<h1>404 - Page Not Found</h1><p>The requested resource does not exist.</p>", status_code=404)

@app.exception_handler(500)
async def internal_server_error_handler(request: Request, exc):
    if request.url.path.startswith("/api/"):
        return JSONResponse(status_code=500, content={"error": "Internal server error"})
    return HTMLResponse(content="<h1>500 - Internal Server Error</h1><p>An unexpected error occurred.</p>", status_code=500)


@app.get("/", response_class=HTMLResponse)
def pagina_locard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dr. Edmond Locard - Criminology & Forensic Science</title>

        <!-- RECOMENDACIÓN: Icono de la página (Favicon) -->
        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">

        <!-- Bootstrap 5 -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Google Fonts & FontAwesome -->
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        
        <style>
            :root {
                --bg-dark: #0f172a;
                --card-bg: #1e293b;
                --accent-blue: #38bdf8;
                --gold: #f59e0b;
                --text-main: #f8fafc;
            }

            body {
                background-color: var(--bg-dark);
                color: var(--text-main);
                font-family: 'Inter', sans-serif;
                overflow-x: hidden;
            }

            h1, h2, h3, .font-heading {
                font-family: 'Cinzel', serif;
            }

            /* Animated Header */
            .hero-section {
                background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.9)), 
                            url('/static/images 3.jpg') center top/cover;
                padding: 80px 0 60px 0;
                border-bottom: 2px solid rgba(56, 189, 248, 0.2);
            }

            .hero-title {
                font-size: 3.5rem;
                color: #ffffff;
                text-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
            }

            .badge-forensic {
                background: rgba(56, 189, 248, 0.1);
                color: var(--accent-blue);
                border: 1px solid var(--accent-blue);
                letter-spacing: 2px;
            }

            .locard-portrait-header {
                width: 170px;
                height: 170px;
                object-fit: cover;
                border-radius: 50%;
                border: 3px solid var(--accent-blue);
                box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
            }

            /* History & Custom Cards */
            .history-card, .custom-info-card {
                background: var(--card-bg);
                border-left: 4px solid var(--accent-blue);
                padding: 25px;
                border-radius: 8px;
                margin-bottom: 25px;
            }

            .fact-card {
                background: var(--card-bg);
                border-left: 4px solid var(--gold);
                padding: 20px;
                border-radius: 8px;
                height: 100%;
            }

            .conditional-card {
                background: var(--card-bg);
                border: 1px solid rgba(56, 189, 248, 0.3);
                border-radius: 8px;
                padding: 20px;
                height: 100%;
            }

            /* Methodology Cards Gallery */
            .method-card {
                background: var(--card-bg);
                border: 1px solid rgba(56, 189, 248, 0.2);
                border-radius: 12px;
                overflow: hidden;
                transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
                height: 100%;
                display: flex;
                flex-direction: column;
            }

            .method-card:hover {
                transform: translateY(-5px);
                border-color: var(--accent-blue);
                box-shadow: 0 10px 20px rgba(56, 189, 248, 0.25);
            }

            .method-card img {
                width: 100%;
                height: 170px;
                object-fit: cover;
            }

            .method-card-body {
                padding: 15px;
                display: flex;
                flex-direction: column;
                flex-grow: 1;
            }

            .method-title {
                font-size: 1.05rem;
                color: var(--accent-blue);
                margin-bottom: 8px;
            }

            .method-text {
                font-size: 0.85rem;
                color: #94a3b8;
                line-height: 1.4;
            }

            .method-badge {
                font-size: 0.75rem;
                background: rgba(245, 158, 11, 0.15);
                color: var(--gold);
                border: 1px solid var(--gold);
                padding: 3px 8px;
                border-radius: 4px;
                display: inline-block;
                margin-bottom: 8px;
            }

            /* Estilos para la sección de Posts de Admiración */
            .post-card {
                background: var(--card-bg);
                border: 1px solid rgba(56, 189, 248, 0.25);
                border-radius: 10px;
                padding: 20px;
                height: 100%;
            }

            .post-header {
                font-size: 0.9rem;
                color: var(--accent-blue);
                border-bottom: 1px solid rgba(255,255,255,0.1);
                padding-bottom: 8px;
                margin-bottom: 12px;
            }

            /* Estilos para el Footer */
            footer {
                background-color: #090d16;
                border-top: 1px solid rgba(56, 189, 248, 0.2);
                padding: 30px 0;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>

        <!-- HEADER WITH PORTRAIT -->
        <header class="hero-section text-center">
            <div class="container">
                <img src="/static/images 3.jpg" alt="Dr. Edmond Locard Portrait" class="locard-portrait-header mb-3">
                <br>
                <span class="badge badge-forensic px-3 py-2 rounded-pill mb-3">CRIMINOLOGY & FORENSIC SCIENCE</span>
                <h1 class="hero-title fw-bold">Dr. Edmond Locard</h1>
                <p class="lead text-info">1877 – 1966 | Scientific Pioneer & Investigator</p>
            </div>
        </header>

        <main class="container my-5">

            <!-- DETAILED HISTORY AND FEATURED PORTRAITS -->
            <section class="mb-5">
                <h2 class="text-warning font-heading mb-4"><i class="fa-solid fa-book-open me-2"></i>Extensive History & Legacy</h2>

                <div class="row align-items-center mb-4">
                    <div class="col-md-4 text-center mb-3 mb-md-0">
                        <img src="/static/locard joven y adulto.jpg" alt="Locard in the laboratory" class="img-fluid rounded shadow">
                        <small class="text-muted d-block mt-2">Dr. Edmond Locard in his laboratory</small>
                    </div>
                    <div class="col-md-8">
                        <div class="history-card mb-0">
                            <h4 class="text-info font-heading">1. Early Life and Academic Background</h4>
                            <p class="text-secondary mb-0">Born in Saint-Chamond, France, Locard showed an interdisciplinary interest from an early age. He graduated in both Medicine and Law from the University of Lyon. He was a direct pupil of Alexandre Lacassagne, one of the founders of criminal anthropology. This unique combination of medical and legal knowledge allowed him to understand that criminal investigation needed to move away from empiricism and embrace the scientific method.</p>
                        </div>
                    </div>
                </div>

                <div class="history-card">
                    <h4 class="text-info font-heading">2. The Birth of Scientific Police Work (1910)</h4>
                    <p class="text-secondary mb-0">In 1910, after persistently persuading the police authorities of Lyon, he was granted two attic rooms in the Palais de Justice. Armed with little more than a borrowed microscope and spectroscope, he established the <strong>world's first crime laboratory</strong>. Despite initial skepticism, his successful resolution of complex cases using microscopic analyses of dust and fibers earned him international prestige.</p>
                </div>

                <div class="row align-items-center mb-4">
                    <div class="col-md-8">
                        <div class="history-card mb-0">
                            <h4 class="text-info font-heading">3. The Exchange Principle and Trace Evidence</h4>
                            <p class="text-secondary mb-0">Locard immortalized the universal criminological axiom: <em>"Tout contact laisse une trace"</em> (<strong>"Every contact leaves a trace"</strong>). He maintained that it is impossible for a criminal to act at a crime scene without leaving microscopic traces (dust, pollen, clothing fibers, hair, fluids) or without taking micro-evidence of the environment away with them.</p>
                        </div>
                    </div>
                    <div class="col-md-4 text-center mt-3 mt-md-0">
                        <img src="/static/images 2 .jpg" alt="Commemorative Stamp" class="img-fluid rounded shadow">
                        <small class="text-muted d-block mt-2">Commemorative stamp of Edmond Locard</small>
                    </div>
                </div>

                <div class="history-card">
                    <h4 class="text-info font-heading">4. Technical Innovations and Master Treatise</h4>
                    <p class="text-secondary mb-0">Among his greatest contributions is <strong>Poroscopy</strong>, the detailed study of sweat pores on friction ridges when fingerprints are incomplete. He published his monumental seven-volume work, <em>"Traité de Criminalistique"</em>, which served as the foundational bible for modern forensic science.</p>
                </div>
            </section>

            <!-- FUN FACTS SECTION -->
            <section class="mb-5">
                <h2 class="text-warning font-heading mb-4"><i class="fa-solid fa-lightbulb me-2"></i>Fun Facts About Dr. Locard</h2>
                <div class="row g-4">
                    <div class="col-md-4">
                        <div class="fact-card">
                            <h5 class="text-warning"><i class="fa-solid fa-user-ninja me-2"></i>"The Sherlock Holmes of France"</h5>
                            <p class="text-secondary small mb-0">Arthur Conan Doyle's fictional detective inspired Locard to create his real-life crime lab. In return, contemporaries famously nicknamed Locard the "Sherlock Holmes of France."</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="fact-card">
                            <h5 class="text-warning"><i class="fa-solid fa-building me-2"></i>Humble Beginnings</h5>
                            <p class="text-secondary small mb-0">The world's first police crime laboratory started in a tiny, dusty attic with only two assistants and equipment borrowed from nearby universities.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="fact-card">
                            <h5 class="text-warning"><i class="fa-solid fa-gem me-2"></i>The Counterfeit Case</h5>
                            <p class="text-secondary small mb-0">Locard solved a major counterfeit coin case by analyzing dust trapped under suspects' fingernails, proving they had been handling specific alloy metals.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- CONDITIONAL FORENSIC LOGIC SECTION -->
            <section class="mb-5">
                <h2 class="text-warning font-heading mb-4"><i class="fa-solid fa-diagram-project me-2"></i>Locard's Forensic "If-Then" Rules</h2>
                <div class="row g-4">
                    <div class="col-md-6">
                        <div class="conditional-card">
                            <h5 class="text-info"><i class="fa-solid fa-fingerprint me-2"></i>Partial Fingerprints</h5>
                            <p class="text-secondary small mb-0"><strong>IF</strong> a fingerprint gathered from the crime scene is incomplete or smudged, <strong>THEN</strong> apply <em>Poroscopy</em> to compare the exact counts and positions of sweat pores on the ridge structures.</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="conditional-card">
                            <h5 class="text-info"><i class="fa-solid fa-shirt me-2"></i>Clothing & Dust Analysis</h5>
                            <p class="text-secondary small mb-0"><strong>IF</strong> a suspect denies being present at a specific location, <strong>THEN</strong> extract microscopic dust particles from their garments to verify geographic and occupational origin.</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="conditional-card">
                            <h5 class="text-info"><i class="fa-solid fa-pen-nib me-2"></i>Anonymous Letters</h5>
                            <p class="text-secondary small mb-0"><strong>IF</strong> handwriting appears disguised on questioned documents, <strong>THEN</strong> evaluate stroke pressure, ink composition, and paper fiber to identify the writer.</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="conditional-card">
                            <h5 class="text-info"><i class="fa-solid fa-bullseye me-2"></i>Ballistic Evidence</h5>
                            <p class="text-secondary small mb-0"><strong>IF</strong> spent shell casings are recovered near the scene, <strong>THEN</strong> examine microscopic striations to match the casing precisely to a suspected weapon's barrel.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- GALERÍA DE 20 MÉTODOS Y BUSCADOR INTERACTIVO -->
            <section class="mb-5">
                <div class="d-flex justify-content-between align-items-center flex-wrap mb-4">
                    <h2 class="text-warning font-heading mb-2 mb-md-0"><i class="fa-solid fa-microscope me-2"></i>20 Forensic Methods & Investigations</h2>
                    <div style="width: 300px;">
                        <input type="text" id="buscadorMetodos" class="form-control bg-dark text-white border-info form-control-sm" placeholder="🔍 Filter methods...">
                    </div>
                </div>
                
                <div class="row g-4" id="contenedorMetodos">
                    <!-- 1 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Optical Microscopy.jpg" alt="Locard Optical Microscopy">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">1. Optical Microscopy</h5>
                                <p class="method-text">Dr. Edmond Locard examining trace dust particles under his brass optical microscope in the Lyon attic laboratory.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 2 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Friction Ridge Poroscopy.jpg" alt="Locard Poroscopy Study">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">2. Friction Ridge Poroscopy</h5>
                                <p class="method-text">Dr. Locard meticulously mapping sweat pore patterns from incomplete criminal friction ridge impressions.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 3 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Dust Particles Analysis.jpg" alt="Locard Dust Analysis">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">3. Dust Particles Analysis</h5>
                                <p class="method-text">Dr. Edmond Locard scraping micro-dust from suspect garments to deduce their geographic origin.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 4 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Questioned Documents.jpg" alt="Locard Questioned Documents">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">4. Questioned Documents</h5>
                                <p class="method-text">Dr. Locard scrutinizing ink pigments and paper fibers under magnification to unmask anonymous forgers.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 5 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Trace Evidence.jpg" alt="Locard Trace Evidence">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">5. Trace Evidence</h5>
                                <p class="method-text">Dr. Edmond Locard demonstrating his Exchange Principle by isolating transfer materials at a scene.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 6 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Bullet Striation Studies.jpg" alt="Locard Ballistic Examination">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">6. Bullet Striation Studies</h5>
                                <p class="method-text">Dr. Locard comparing microscopic striations on recovered casings against test-fired rounds.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 7 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Medical Serology.jpg" alt="Locard Medical Serology">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">7. Medical Serology</h5>
                                <p class="method-text">Dr. Edmond Locard testing chemical reagents to classify organic bloodstains recovered from evidence.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 8 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Chemical Toxicology.jpg" alt="Locard Toxicology Assays">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">8. Chemical Toxicology</h5>
                                <p class="method-text">Dr. Locard conducting laboratory assays to extract and identify lethal poisons in criminal cases.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 9 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Metric Photography.jpg" alt="Locard Metric Photography">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">9. Metric Photography</h5>
                                <p class="method-text">Dr. Edmond Locard positioning early vintage cameras to document undisturbed crime scenes with precision.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 10 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Forensic Cryptography.jpg" alt="Locard Cryptography Analysis">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">10. Forensic Cryptography</h5>
                                <p class="method-text">Dr. Locard decoding encrypted criminal ciphers and hidden gang communications in his study.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 11 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Medical Autopsy.jpg" alt="Locard Pathology Autopsy">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">11. Medical Autopsy</h5>
                                <p class="method-text">As a forensic pathologist, Dr. Edmond Locard evaluating physical trauma and weapon impact patterns.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 12 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Latent Print Development.jpg" alt="Locard Latent Print Fuming">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">12. Latent Print Development</h5>
                                <p class="method-text">Dr. Locard applying chemical iodine fumes to reveal invisible friction prints on porous surfaces.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 13 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Modus Operandi Profiling.jpg" alt="Locard Profiling Studies">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">13. Modus Operandi Profiling</h5>
                                <p class="method-text">Dr. Edmond Locard mapping recurring behavioral habits to link unsolved regional criminal cases.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 14 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Textile Fiber Comparison.jpg" alt="Locard Textile Comparison">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">14. Textile Fiber Comparison</h5>
                                <p class="method-text">Dr. Locard comparing microscopic garment threads under polarized light to match suspect clothing.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 15 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Crime Scene Preservation.jpg" alt="Locard Scene Inspection">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">15. Crime Scene Preservation</h5>
                                <p class="method-text">Dr. Edmond Locard supervising police officers to enforce strict isolation protocols at a scene.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 16 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Graphonomy & Handwriting.jpg" alt="Locard Graphonomy Analysis">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">16. Graphonomy & Handwriting</h5>
                                <p class="method-text">Dr. Locard measuring calligraphic slants and stroke angles to identify fraudulent handwriting.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 17 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Toolmark Identification.jpg" alt="Locard Toolmark Analysis">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">17. Toolmark Identification</h5>
                                <p class="method-text">Dr. Edmond Locard examining microscopic metal gouges left on forced locks by burglary tools.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 18 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Medical Anthropometry.jpg" alt="Locard Anthropometry Measurements">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">18. Medical Anthropometry</h5>
                                <p class="method-text">Dr. Locard performing skeletal measurements, correlating Bertillonage with fingerprint records.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 19 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Chain of Custody Protocol.jpg" alt="Locard Custody Protocol">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">19. Chain of Custody Protocol</h5>
                                <p class="method-text">Dr. Edmond Locard signing sterile evidence envelopes to ensure strict judicial traceability.</p>
                            </div>
                        </div>
                    </div>
                    <!-- 20 -->
                    <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="method-card">
                            <img src="/static/Forensic Planimetry.jpg" alt="Locard Forensic Planimetry">
                            <div class="method-card-body">
                                <span class="method-badge">Locard's Method</span>
                                <h5 class="method-title">20. Forensic Planimetry</h5>
                                <p class="method-text">Dr. Locard drafting detailed scale floor plans mapping precise crime scene spatial dynamics.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SIMULADOR INTERACTIVO AMPLIADO A 35 CASOS -->
            <section class="mb-5">
                <div class="history-card border-warning">
                    <h3 class="text-warning font-heading"><i class="fa-solid fa-wand-magic-sparkles me-2"></i>Interactive Exchange Principle Simulator (35 Scenarios)</h3>
                    <p class="text-secondary">Test how Dr. Locard would apply the transfer principle across 35 distinct investigative environments:</p>
                    
                    <div class="mb-3">
                        <label class="form-label text-info">Select a crime scene context:</label>
                        <select id="tipoEscena" class="form-select bg-dark text-white border-secondary">
                            <option value="1">1. Room struggle with carpet and dust</option>
                            <option value="2">2. Firearm discharge in a closed room</option>
                            <option value="3">3. Handling questioned anonymous documents</option>
                            <option value="4">4. Counterfeit coin manufacturing workshop</option>
                            <option value="5">5. Break-in via wooden window frame using a crowbar</option>
                            <option value="6">6. Vehicle hit-and-run leaving paint chips on a victim</option>
                            <option value="7">7. Poisoning case involving chemical plant residue</option>
                            <option value="8">8. Outdoor crime scene in muddy forest terrain</option>
                            <option value="9">9. Arson investigation with accelerant traces</option>
                            <option value="10">10. Physical assault inside a leather-upholstered vehicle</option>
                            <option value="11">11. Burglary involving safe-cracking tools and metal dust</option>
                            <option value="12">12. Kidnapping scene with transfer of pet hairs and fibers</option>
                            <option value="13">13. Industrial workplace accident involving machinery oil</option>
                            <option value="14">14. Stabbing in a kitchen leaving microscopic blade fragments</option>
                            <option value="15">15. Smuggling case involving specific soil and mineral pollens</option>
                            <option value="16">16. Nightclub altercation with cosmetic and powder transfers</option>
                            <option value="17">17. Warehouse theft involving cardboard and packaging lint</option>
                            <option value="18">18. High-speed highway collision with glass shattering</option>
                            <option value="19">19. Boat piracy involving salt crystals and marine algae</option>
                            <option value="20">20. Train compartment robbery with textile seat friction</option>
                            <option value="21">21. Art gallery forgery involving canvas and old oil pigments</option>
                            <option value="22">22. Pharmacy break-in leaving medicinal pill fragments</option>
                            <option value="23">23. Construction site accident with cement and drywall dust</option>
                            <option value="24">24. Cybercrime investigation involving printer toner particles</option>
                            <option value="25">25. Rural barn crime scene with agricultural grain husks</option>
                            <option value="26">26. Mountain cabin burglary with fireplace soot and ash</option>
                            <option value="27">27. Jewelry store heist involving velvet display tray lint</option>
                            <option value="28">28. Subterranean sewer or tunnel escape with mineral lime</option>
                            <option value="29">29. Airport tarmac security breach with jet fuel residue</option>
                            <option value="30">30. Botanical garden crime scene with exotic plant spores</option>
                            <option value="31">31. Textile mill theft with colored synthetic thread traces</option>
                            <option value="32">32. Bakery break-in leaving flour and sugar micro-granules</option>
                            <option value="33">33. Steel foundry altercation with carbon and iron flakes</option>
                            <option value="34">34. Library archive tampering with antique paper acidity</option>
                            <option value="35">35. Seaside resort theft with coastal sand and salt spray</option>
                        </select>
                    </div>
                    <button type="button" class="btn btn-outline-warning" onclick="analizarEvidencia()">Analyze with Locard's Law</button>
                    
                    <div id="resultadoLocard" class="mt-3 text-info fw-bold"></div>
                </div>
            </section>

            <!-- 20 POSTS COMPLETOS BASADOS EN LAS INSTRUCCIONES DE LA GUÍA -->
            <section class="mb-5">
                <h2 class="text-warning font-heading mb-4"><i class="fa-solid fa-comments me-2"></i>20 Academic Profile Posts for Dr. Edmond Locard</h2>
                <div class="row g-4">
                    <!-- Post 1 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-user me-2"></i><strong>Post 1: Introduction, Birth Place & Date</strong></div>
                            <p class="text-light small mb-0">Dr. Edmond Locard was born on December 13, 1877, in Saint-Chamond, France. As a fundamental pioneer in criminology and forensic science, he devoted his life to transforming criminal investigation into an objective science.</p>
                        </div>
                    </div>
                    <!-- Post 2 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-brain me-2"></i><strong>Post 2: Early Signs of Intelligence Type</strong></div>
                            <p class="text-light small mb-0">From an early age, Locard demonstrated exceptional logical-mathematical intelligence, showing a remarkable ability to observe subtle natural phenomena and connect disparate physical evidence logically.</p>
                        </div>
                    </div>
                    <!-- Post 3 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-compass me-2"></i><strong>Post 3: Primary Motivations & Vocational Interests</strong></div>
                            <p class="text-light small mb-0">Locard's primary motivation was replacing unreliable subjective testimony with unyielding scientific truth, driven by a deep desire to ensure judicial justice through undeniable physical evidence.</p>
                        </div>
                    </div>
                    <!-- Post 4 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-microscope me-2"></i><strong>Post 4: First Exposure to Forensic Study</strong></div>
                            <p class="text-light small mb-0">His first exposure to criminalistics occurred during his university years in Lyon, where he recognized that police investigations lacked rigorous scientific methodologies.</p>
                        </div>
                    </div>
                    <!-- Post 5 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-graduation-cap me-2"></i><strong>Post 5: Entrance into Higher Education</strong></div>
                            <p class="text-light small mb-0">Locard entered the University of Lyon, completing rigorous professional training in both Medicine and Law, equipping him with clinical insight and legal expertise.</p>
                        </div>
                    </div>
                    <!-- Post 6 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-people-arrows me-2"></i><strong>Post 6: Key Mentors & Career Influences</strong></div>
                            <p class="text-light small mb-0">Professor Alexandre Lacassagne served as his primary mentor, while Arthur Conan Doyle's fictional detective Sherlock Holmes inspired his real-world investigative focus.</p>
                        </div>
                    </div>
                    <!-- Post 7 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-award me-2"></i><strong>Post 7: Graduate Profile & Key Skills</strong></div>
                            <p class="text-light small mb-0">He developed advanced skills in microscopic dust analysis, chemical testing, document examination, and meticulous observation, bridging biological science with legal standards.</p>
                        </div>
                    </div>
                    <!-- Post 8 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-briefcase me-2"></i><strong>Post 8: First Official Job & Research Project</strong></div>
                            <p class="text-light small mb-0">In 1910, Locard established the first police crime lab in two attic rooms in Lyon, focusing his initial research on fingernail dust analysis and micro-fibers.</p>
                        </div>
                    </div>
                    <!-- Post 9 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-book me-2"></i><strong>Post 9: Major Contribution & Publication</strong></div>
                            <p class="text-light small mb-0">His most famous contribution is the Exchange Principle ("Every contact leaves a trace"), alongside inventing poroscopy and writing the monumental "Traité de Criminalistique".</p>
                        </div>
                    </div>
                    <!-- Post 10 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-trophy me-2"></i><strong>Post 10: Recognition & Historical Milestones</strong></div>
                            <p class="text-light small mb-0">Known as "The Sherlock Holmes of France", Locard received worldwide acclaim, permanently establishing international forensic science academies and crime laboratories.</p>
                        </div>
                    </div>
                    <!-- Post 11 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-quote-left me-2"></i><strong>Post 11: Famous Quote</strong></div>
                            <p class="text-light small mb-0">"Tout contact laisse une trace" (Every contact leaves a trace)—Locard's legendary quote encapsulates the core axiom governing all modern physical evidence recovery.</p>
                        </div>
                    </div>
                    <!-- Post 12 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-shuffle me-2"></i><strong>Post 12: Transformation of the Field</strong></div>
                            <p class="text-light small mb-0">Locard transformed criminology from a speculative art into an empirical science, proving that silent physical evidence speaks louder than coerced confessions.</p>
                        </div>
                    </div>
                    <!-- Post 13 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-triangle-exclamation me-2"></i><strong>Post 13: Major Career Obstacle</strong></div>
                            <p class="text-light small mb-0">Locard faced severe initial skepticism and budget resistance from conservative police authorities who preferred traditional, subjective interrogation methods over microscopy.</p>
                        </div>
                    </div>
                    <!-- Post 14 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-code-branch me-2"></i><strong>Post 14: Third Conditional Analysis</strong></div>
                            <p class="text-light small mb-0">If Locard hadn't persevered against bureaucratic rejection in Lyon, modern forensic laboratories would not have emerged as early as 1910, delaying scientific crime solving globally.</p>
                        </div>
                    </div>
                    <!-- Post 15 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-clock-rotate-left me-2"></i><strong>Post 15: Hypothetical Past Decision</strong></div>
                            <p class="text-light small mb-0">If Locard had chosen exclusively to practice medicine instead of combining it with law, he might never have created the universal framework for forensic jurisprudence.</p>
                        </div>
                    </div>
                    <!-- Post 16 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-shield-halved me-2"></i><strong>Post 16: Overcoming Adversity</strong></div>
                            <p class="text-light small mb-0">He overcame institutional resistance by proving his methods through undeniable casework success, turning a tiny, dusty attic into a world-renowned scientific institution.</p>
                        </div>
                    </div>
                    <!-- Post 17 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-laptop-code me-2"></i><strong>Post 17: Connection with Modern Technology</strong></div>
                            <p class="text-light small mb-0">Locard's exchange principle forms the foundational logic behind today's advanced digital forensics, DNA profiling, mass spectrometry, and automated fingerprint identification.</p>
                        </div>
                    </div>
                    <!-- Post 18 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-graduation-cap me-2"></i><strong>Post 18: Advice for 11th Grade Students</strong></div>
                            <p class="text-light small mb-0">"Never stop questioning assumptions, remain passionately curious, and always let objective data guide your conclusions rather than preconceived biases."</p>
                        </div>
                    </div>
                    <!-- Post 19 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-image me-2"></i><strong>Post 19: Lasting Professional Legacy</strong></div>
                            <p class="text-light small mb-0">His enduring legacy lives on in every crime lab worldwide, reminding investigators that every action leaves a microscopic signature waiting to be discovered.</p>
                        </div>
                    </div>
                    <!-- Post 20 -->
                    <div class="col-md-6">
                        <div class="post-card">
                            <div class="post-header"><i class="fa-solid fa-shield-cat me-2"></i><strong>Post 20: Closing Message on Digital Responsibility</strong></div>
                            <p class="text-light small mb-0">Just as physical contact leaves physical traces, our digital actions leave permanent footprints. We must exercise ethics, truth, and responsibility in the digital age.</p>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <!-- Pie de página informativo -->
        <footer class="text-center text-muted">
            <div class="container">
                <p class="mb-1">Dr. Edmond Locard Forensic Science Educational Portal</p>
                <small>&copy; FastAPI Criminology Showcase - Powered by Locard's Exchange Principle</small>
            </div>
        </footer>

        <!-- SCRIPT PARA EL BUSCADOR Y EL SIMULADOR DE 35 CASOS -->
        <script>
            document.getElementById('buscadorMetodos').addEventListener('keyup', function() {
                let filtro = this.value.toLowerCase();
                let tarjetas = document.querySelectorAll('#contenedorMetodos > div');
                tarjetas.forEach(function(card) {
                    let texto = card.textContent.toLowerCase();
                    if (texto.includes(filtro)) {
                        card.style.display = "";
                    } else {
                        card.style.display = "none";
                    }
                });
            });

            function analizarEvidencia() {
                let val = document.getElementById('tipoEscena').value;
                let salida = document.getElementById('resultadoLocard');
                
                const resultados = {
                    "1": "Result: Massive transfer of textile fibers, hairs, and micro-dust particles between the suspect and the carpet.",
                    "2": "Result: Deposition of gunshot residue (barium, antimony, lead) on the shooter's hands and microscopic striations on the casing.",
                    "3": "Result: Transfer of writing pressure, chemical ink components, and paper micro-fibers.",
                    "4": "Result: Alloy dust under fingernails matching counterfeit coin metal compositions.",
                    "5": "Result: Wood splinters and paint flakes embedded in the crowbar tool edge.",
                    "6": "Result: Microscopic automotive paint layers transferred to the victim's clothing.",
                    "7": "Result: Traces of specific industrial chemical reagents found in biological tissue assays.",
                    "8": "Result: Unique mud composition, clay types, and weed pollens adhered to footwear soles.",
                    "9": "Result: Hydrocarbon residues and volatile accelerants trapped in surrounding porous materials.",
                    "10": "Result: Synthetic leather particles and driver seat fabric strands transferred to jacket.",
                    "11": "Result: Safe insulation powder and microscopic metal shavings on suspect clothing.",
                    "12": "Result: Animal dander and specialized carpet fibers transferred during confinement.",
                    "13": "Result: Heavy machinery lubricants and industrial grease trapped in fabric weave.",
                    "14": "Result: Microscopic metal particles from the knife tip left inside wound tissue.",
                    "15": "Result: Regional pollens and mineral soils matching origin country found in luggage lining.",
                    "16": "Result: Facial cosmetic powder traces transferred through skin-to-skin or garment contact.",
                    "17": "Result: Corrugated cardboard dust and cellulose micro-fibers found on suspect gloves.",
                    "18": "Result: Tempered glass fragments embedded in bumper grooves and clothing cuffs.",
                    "19": "Result: Marine plankton, salt crusts, and damp wood fibers found on deck gear.",
                    "20": "Result: Upholstery synthetic plush fibers matching train compartment seating.",
                    "21": "Result: Linseed oil degradation markers and historical pigment mineral traces.",
                    "22": "Result: Crystalline pharmaceutical powder traces on pockets and zipper tracks.",
                    "23": "Result: Portland cement dust and gypsum micro-particles embedded in boots.",
                    "24": "Result: Laser printer toner micro-particles and drum heat impressions on paper.",
                    "25": "Result: Wheat or corn starch husks and barnyard straw debris on garments.",
                    "26": "Result: Hardwood creosote, ash, and carbon soot particles in clothing pores.",
                    "27": "Result: Premium velvet fabric lint and gold-plating micro-dust flakes.",
                    "28": "Result: Calcium carbonate (lime) scaling and damp subterranean soil microbes.",
                    "29": "Result: Jet fuel (Kerosene) hydrocarbon traces and runway rubber particles.",
                    "30": "Result: Rare greenhouse fern spores and exotic fertilizer components.",
                    "31": "Result: Specialized dyed synthetic filament strands caught in machinery.",
                    "32": "Result: Bleached wheat flour granules and granulated sugar crystals in seams.",
                    "33": "Result: Iron oxide scale, carbon slag, and foundry furnace particulate matter.",
                    "34": "Result: Cellulose degradation byproducts, mold spores, and antique book glue.",
                    "35": "Result: Fine quartz coastal sand grains and sodium chloride salt crystals."
                };

                salida.innerHTML = resultados[val] || "Result: General trace evidence exchange verified.";
            }
        </script>
    </body>
    </html>
    """

# Endpoint de API complementario
@app.get("/api/locard/metodos")
def obtener_metodos():
    return {
        "pionero": "Dr. Edmond Locard",
        "principio_fundamental": "Tout contact laisse une trace (Every contact leaves a trace)",
        "total_metodos": 20,
        "simulador_escenarios": 35,
        "posts_admiracion": 20,
        "estado": "Activo y funcionando"
    }
