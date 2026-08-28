// Proxy para Google Places API (New) - Place Details (reviews).
// La API key vive solo en variables de entorno de Netlify (GOOGLE_API_KEY,
// GOOGLE_PLACE_ID), nunca en el repo. El Cache-Control de la respuesta deja
// que la CDN de Netlify sirva la misma respuesta cacheada durante 24h en vez
// de llamar a Google en cada visita.

export default async () => {
  const apiKey = process.env.GOOGLE_API_KEY;
  const placeId = process.env.GOOGLE_PLACE_ID;

  if (!apiKey || !placeId) {
    return new Response(JSON.stringify({ error: 'not_configured' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const url = `https://places.googleapis.com/v1/places/${placeId}?fields=rating,userRatingCount,reviews&languageCode=es`;

  let googleRes;
  try {
    googleRes = await fetch(url, {
      headers: { 'X-Goog-Api-Key': apiKey },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'network_error' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  if (!googleRes.ok) {
    return new Response(JSON.stringify({ error: 'api_error', http_code: googleRes.status }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const data = await googleRes.json();

  const result = {
    rating: data.rating ?? null,
    userRatingCount: data.userRatingCount ?? null,
    reviews: (data.reviews ?? []).map((r) => ({
      author: r.authorAttribution?.displayName ?? '',
      text: r.text?.text ?? r.originalText?.text ?? '',
      rating: r.rating ?? 5,
      relativeTime: r.relativePublishTimeDescription ?? '',
    })),
  };

  return new Response(JSON.stringify(result), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=86400',
    },
  });
};
