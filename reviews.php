<?php
/**
 * Proxy para Google Places API (New) - Place Details (reviews).
 * Esconde la API key del navegador y cachea el resultado 24h en disco
 * para no gastar la cuota gratuita ni exponer la clave en el HTML.
 */

// --- CONFIGURA ESTOS DOS VALORES ---
const GOOGLE_API_KEY = 'AIzaSyABymwZI2-UVZttVDvykJwYGF67HiLPd4A';
const GOOGLE_PLACE_ID = 'ChIJrbv6t_UPYw0RIqlITjokoNI';
// ------------------------------------

const CACHE_FILE = __DIR__ . '/cache/reviews_cache.json';
const CACHE_TTL_SECONDS = 86400; // 24 horas

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

function respond($data) {
    echo json_encode($data);
    exit;
}

// Servir desde caché si es reciente
if (is_file(CACHE_FILE) && (time() - filemtime(CACHE_FILE) < CACHE_TTL_SECONDS)) {
    respond(json_decode(file_get_contents(CACHE_FILE), true));
}

if (GOOGLE_API_KEY === 'TU_API_KEY_AQUI' || GOOGLE_PLACE_ID === 'TU_PLACE_ID_AQUI') {
    respond(['error' => 'not_configured']);
}

$url = 'https://places.googleapis.com/v1/places/' . GOOGLE_PLACE_ID
     . '?fields=rating,userRatingCount,reviews'
     . '&languageCode=es';

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'X-Goog-Api-Key: ' . GOOGLE_API_KEY,
    ],
    CURLOPT_TIMEOUT => 10,
]);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpCode !== 200 || !$response) {
    // Si falla la llamada y hay caché vieja, mejor servir eso que nada
    if (is_file(CACHE_FILE)) {
        respond(json_decode(file_get_contents(CACHE_FILE), true));
    }
    respond(['error' => 'api_error', 'http_code' => $httpCode]);
}

$data = json_decode($response, true);

$result = [
    'rating' => $data['rating'] ?? null,
    'userRatingCount' => $data['userRatingCount'] ?? null,
    'reviews' => array_map(function ($r) {
        return [
            'author' => $r['authorAttribution']['displayName'] ?? '',
            'text' => $r['text']['text'] ?? ($r['originalText']['text'] ?? ''),
            'rating' => $r['rating'] ?? 5,
            'relativeTime' => $r['relativePublishTimeDescription'] ?? '',
        ];
    }, $data['reviews'] ?? []),
];

if (!is_dir(__DIR__ . '/cache')) {
    mkdir(__DIR__ . '/cache', 0755, true);
}
file_put_contents(CACHE_FILE, json_encode($result));

respond($result);
