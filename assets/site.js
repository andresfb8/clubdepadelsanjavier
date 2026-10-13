// Club de Pádel San Javier — lógica compartida
(function () {
    const lang = document.documentElement.lang === 'en' ? 'en' : 'es';
    document.documentElement.classList.add('js');

    // --- CABECERA ---
    const header = document.querySelector('.header');
    if (header && !header.classList.contains('header--solid')) {
        const onScroll = () => header.classList.toggle('is-solid', window.scrollY > 40);
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    // --- MENÚ MÓVIL ---
    const menu = document.getElementById('menu');
    const burger = document.querySelector('.burger');
    if (menu && burger) {
        const setMenu = (open) => {
            menu.classList.toggle('is-open', open);
            document.body.classList.toggle('menu-open', open);
            burger.setAttribute('aria-expanded', String(open));
            if (open) menu.querySelector('.menu__close').focus();
            else burger.focus();
        };
        burger.addEventListener('click', () => setMenu(true));
        menu.querySelector('.menu__close').addEventListener('click', () => setMenu(false));
        menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => {
            menu.classList.remove('is-open');
            document.body.classList.remove('menu-open');
            burger.setAttribute('aria-expanded', 'false');
        }));
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && menu.classList.contains('is-open')) setMenu(false);
        });
    }

    // --- VÍDEO DEL HERO ---
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const heroVideo = document.querySelector('video.hero__media');
    if (heroVideo && reduceMotion) {
        heroVideo.removeAttribute('autoplay');
        heroVideo.pause();
    }

    // --- DATOS: ENTRENADORES ---
    const coaches = [
        { name: 'Dani', image: '/img/dani.jpg', role: { es: 'Coordinador del club', en: 'Club coordinator' }, shot: { es: 'La víbora letal', en: 'The lethal víbora' } },
        { name: 'Alberto', image: '/img/alberto.jpg', role: { es: 'Escuela de menores y adultos', en: 'Kids and adults coach' }, shot: { es: 'El globo infinito', en: 'The endless lob' } },
        { name: 'Carlos', image: '/img/carlos.jpg', role: { es: 'Escuela de menores y adultos', en: 'Kids and adults coach' }, shot: { es: 'Volea de bloqueo', en: 'Block volley' } },
        { name: 'Jorge', image: '/img/jorge.jpg', role: { es: 'Escuela de menores', en: 'Kids coach' }, shot: { es: 'Bajada de pared', en: 'Off-the-wall smash' } },
        { name: 'Pedro', image: '/img/pedro.jpg', role: { es: 'Escuela de adultos', en: 'Adults coach' }, shot: { es: 'El remate x3', en: 'The x3 smash' } },
        { name: 'Antonio', image: '/img/antonio.jpg', role: { es: 'Escuela de adultos', en: 'Adults coach' }, shot: { es: 'Saque con efecto', en: 'Spin serve' } },
    ];

    function el(tag, className, text) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (text !== undefined) node.textContent = text;
        return node;
    }

    const team = document.querySelector('[data-team]');
    if (team) {
        const limit = Number(team.dataset.team) || coaches.length;
        coaches.slice(0, limit).forEach((coach) => {
            const card = el('article', 'coach');
            const img = el('img');
            img.src = coach.image;
            img.alt = coach.name;
            img.loading = 'lazy';
            const info = el('div', 'coach__info');
            info.append(el('h3', '', coach.name), el('p', '', coach.role[lang]), el('span', 'coach__shot', coach.shot[lang]));
            card.append(img, info);
            team.append(card);
        });
    }

    // --- DATOS: RESEÑAS FIJAS (respaldo si /api/reviews no responde) ---
    const fallbackReviews = [
        {
            author: 'Sergio Nuñez',
            time: { es: 'Hace 2 años', en: '2 years ago' },
            text: {
                es: 'Gran club, muy buen ambiente entre todos y monitores de pádel geniales. Es lo que el polideportivo necesitaba , una inyección de Pádel.',
                en: "Great club, very good atmosphere among everyone, and amazing padel instructors. It's what the sports center needed, an injection of Padel.",
            },
        },
        {
            author: 'Alvaro Sanchez',
            time: { es: 'Hace 8 meses', en: '8 months ago' },
            text: {
                es: 'Club de pádel con un excelente personal dispuesto a enseñarte.',
                en: 'Padel club with excellent staff willing to teach you.',
            },
        },
        {
            author: 'Fernando Javier',
            time: { es: 'Hace 5 meses', en: '5 months ago' },
            text: {
                es: 'Ambiente espectacular y monitores muy profesionales, sobre todo Andrés, que es con quien más me relaciono, puesto que es quien me da clases. También hacen mini torneos los viernes para que haya una pequeña convivencia entre todos los alumnos y crear buen ambiente. Lo recomiendo al 100%.',
                en: 'Spectacular atmosphere and very professional instructors, especially Andrés, who is the one I interact with the most, as he gives me classes. They also hold mini-tournaments on Fridays to create a small community among all students and build a good atmosphere. I recommend it 100%.',
            },
        },
        {
            author: 'Patrick Gordinne',
            time: { es: 'Hace 3 meses', en: '3 months ago' },
            text: {
                es: 'Me apunté al club de Padel de San Javier porque no había jugado nunca. Decidí apuntarme para aprender y me esta enseñando el entrenador Dani. Muy profesional, tiene clases de todos los niveles y te enseña desde cero como es mi caso. Incide en la técnica para que mejor dia a dia. Sorprendido con el buen ambiente y buen rollo. Muy recomendable si quieres aprender desde cero o quieres mejorar tu Padel.',
                en: 'I signed up for the San Javier Padel club because I had never played before. I decided to join to learn, and coach Dani is teaching me. Very professional, they have classes for all levels and teach you from scratch, as is my case. He focuses on technique so you improve day by day. Surprised by the good atmosphere and good vibes. Highly recommended if you want to learn from scratch or improve your Padel.',
            },
        },
    ];

    const reviewsBox = document.querySelector('[data-reviews]');
    if (reviewsBox) {
        const limit = Number(reviewsBox.dataset.reviews) || 4;

        const renderReviews = (reviews) => {
            reviewsBox.replaceChildren(...reviews.slice(0, limit).map((review) => {
                const card = el('article', 'review');
                const stars = el('div', 'stars', '★'.repeat(review.rating || 5));
                stars.setAttribute('aria-label', (review.rating || 5) + '/5');
                const footer = el('footer');
                footer.append(el('b', '', review.author), document.createTextNode(review.relativeTime || ''));
                card.append(stars, el('blockquote', '', review.text), footer);
                return card;
            }));
        };

        renderReviews(fallbackReviews.map((r) => ({ author: r.author, text: r.text[lang], relativeTime: r.time[lang], rating: 5 })));

        fetch('/api/reviews?lang=' + lang)
            .then((res) => (res.ok ? res.json() : Promise.reject()))
            .then((data) => {
                if (!data || !Array.isArray(data.reviews)) return;
                const live = data.reviews.filter((r) => r.text);
                if (live.length > 0) renderReviews(live);
                const ratingEl = document.querySelector('[data-rating]');
                if (ratingEl && data.rating) ratingEl.textContent = Number(data.rating).toFixed(1);
            })
            .catch(() => { /* Se queda con las reseñas fijas ya renderizadas */ });
    }

    // --- FORMULARIO (Netlify Forms) ---
    const form = document.querySelector('form[data-netlify]');
    if (form) {
        const msg = form.querySelector('.form__msg');
        const texts = {
            ok: { es: '¡Recibido! Te escribimos muy pronto.', en: "Got it! We'll be in touch very soon." },
            error: { es: 'No se ha podido enviar. Escríbenos por WhatsApp y lo vemos.', en: "That didn't send. Message us on WhatsApp and we'll sort it." },
        };
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const button = form.querySelector('button[type="submit"]');
            button.disabled = true;
            fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(new FormData(form)).toString(),
            })
                .then((res) => {
                    if (!res.ok) throw new Error(res.status);
                    form.reset();
                    msg.dataset.state = 'ok';
                    msg.textContent = texts.ok[lang];
                })
                .catch(() => {
                    msg.dataset.state = 'error';
                    msg.textContent = texts.error[lang];
                })
                .finally(() => { button.disabled = false; });
        });
    }

    // --- APARICIÓN AL HACER SCROLL ---
    const revealEls = document.querySelectorAll('.reveal');
    if (reduceMotion || !('IntersectionObserver' in window)) {
        revealEls.forEach((node) => node.classList.add('is-in'));
    } else {
        const io = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-in');
                    io.unobserve(entry.target);
                }
            });
        }, { rootMargin: '0px 0px -10% 0px' });
        revealEls.forEach((node) => io.observe(node));
    }

    document.querySelectorAll('[data-year]').forEach((node) => { node.textContent = new Date().getFullYear(); });
})();
