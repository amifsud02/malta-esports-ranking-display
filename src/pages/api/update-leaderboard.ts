export async function GET() {
    // Get Data from API
    const response = await fetch('https://open.faceit.com/data/v4/rankings/games/cs2/regions/EU?country=mt&limit=10', {
        headers: {
            'Authorization': `Bearer ${import.meta.env.FACEIT_SERVER_KEY}`
        }
    })

    // Parse Data
    const data = await response.json()
    const { items } = data;
    
    return new Response(
        JSON.stringify({
            items
        }),
    )
}