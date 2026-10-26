/**
 * FlixMatch AI - Consumer Streaming Application Controller
 * Netflix / Prime Video Style Experience
 */

const App = {
  facts: {
    domain: 'both',
    mood: 'reflective',
    companion: 'solo',
    cognitive_load: 'deeply_philosophical',
    tempo: 'slow_burn',
    preferred_era: 'contemporary',
    genre_preferences: ['Sci-Fi']
  },

  currentHeroItem: null,
  allRecommendations: [],
  myWatchlist: JSON.parse(localStorage.getItem('flixmatch_watchlist') || '[]'),
  currentCategoryFilter: 'all',

  async init() {
    this.bindHeaderScroll();
    this.bindEvents();
    await this.fetchRecommendations();
  },

  bindHeaderScroll() {
    window.addEventListener('scroll', () => {
      const header = document.querySelector('header.stream-header');
      if (header) {
        if (window.scrollY > 40) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
      }
    });
  },

  bindEvents() {
    // Nav links
    document.querySelectorAll('.nav-link-item').forEach(item => {
      item.addEventListener('click', (e) => {
        document.querySelectorAll('.nav-link-item').forEach(i => i.classList.remove('active'));
        item.classList.add('active');
        const filter = item.getAttribute('data-filter');
        this.filterCategory(filter);
      });
    });

    // AI Vibe Matcher Drawer Toggle
    const vibeBtn = document.getElementById('btnToggleTuning');
    if (vibeBtn) {
      vibeBtn.addEventListener('click', () => {
        const drawer = document.getElementById('aiTuningDrawer');
        if (drawer) drawer.classList.toggle('open');
      });
    }

    // Mood chips
    document.querySelectorAll('.mood-chip-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.mood-chip-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const moodVal = btn.getAttribute('data-mood');
        const cogVal = btn.getAttribute('data-cog');
        const tempoVal = btn.getAttribute('data-tempo');

        if (moodVal) this.facts.mood = moodVal;
        if (cogVal) this.facts.cognitive_load = cogVal;
        if (tempoVal) this.facts.tempo = tempoVal;

        this.fetchRecommendations();
      });
    });

    // Search bar
    const searchInput = document.getElementById('streamSearchInput');
    if (searchInput) {
      let timeout = null;
      searchInput.addEventListener('input', (e) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => this.handleSearch(e.target.value), 250);
      });
    }

    // Tuning drawer selects
    const companionSelect = document.getElementById('selectCompanion');
    if (companionSelect) {
      companionSelect.addEventListener('change', (e) => {
        this.facts.companion = e.target.value;
        this.fetchRecommendations();
      });
    }
    const tempoSelect = document.getElementById('selectTempo');
    if (tempoSelect) {
      tempoSelect.addEventListener('change', (e) => {
        this.facts.tempo = e.target.value;
        this.fetchRecommendations();
      });
    }
    const cognitiveSelect = document.getElementById('selectCognitive');
    if (cognitiveSelect) {
      cognitiveSelect.addEventListener('change', (e) => {
        this.facts.cognitive_load = e.target.value;
        this.fetchRecommendations();
      });
    }
  },

  async fetchRecommendations() {
    try {
      const res = await fetch('/api/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.facts)
      });
      const data = await res.json();
      if (data.success && data.data) {
        const result = data.data;
        this.allRecommendations = result.recommendations;
        
        // Render Hero Billboard with the top AI match
        if (result.top_match) {
          this.renderHeroBillboard(result.top_match, result.fired_rules);
        }

        // Render Netflix Rows
        this.renderStreamingRows(result.rows);
      }
    } catch (err) {
      console.error('Failed to fetch recommendations:', err);
    }
  },

  renderHeroBillboard(item, firedRules) {
    this.currentHeroItem = item;
    const billboard = document.getElementById('heroBillboard');
    if (!billboard) return;

    billboard.style.backgroundImage = `url('${item.backdrop || item.poster}')`;

    const titleEl = document.getElementById('heroItemTitle');
    const matchEl = document.getElementById('heroMatchScore');
    const yearEl = document.getElementById('heroItemYear');
    const ageEl = document.getElementById('heroItemAge');
    const runtimeEl = document.getElementById('heroItemRuntime');
    const qualityEl = document.getElementById('heroItemQuality');
    const synopsisEl = document.getElementById('heroItemSynopsis');
    const reasonEl = document.getElementById('heroAIReason');

    if (titleEl) titleEl.textContent = item.title;
    if (matchEl) matchEl.textContent = `${item.confidence}% Match`;
    if (yearEl) yearEl.textContent = item.year;
    if (ageEl) ageEl.textContent = item.age_rating || '16+';
    if (runtimeEl) runtimeEl.textContent = item.runtime_or_pages;
    if (qualityEl) qualityEl.textContent = item.quality || '4K Ultra HD';
    if (synopsisEl) synopsisEl.textContent = item.synopsis;

    // Build intelligent natural language explanation from fired rules
    if (reasonEl) {
      const topRule = item.matched_rules && item.matched_rules.length > 0 ? item.matched_rules[0] : null;
      if (topRule) {
        reasonEl.innerHTML = `<span>🧠 FlixMatch AI:</span> ${topRule.explanation}`;
      } else {
        reasonEl.innerHTML = `<span>🧠 FlixMatch AI:</span> Handpicked based on your ${this.facts.mood} mood and ${this.facts.companion} setting.`;
      }
    }

    // Update hero watchlist button state
    this.updateHeroWatchlistButton(item.id);
  },

  renderStreamingRows(rows) {
    const container = document.getElementById('streamingRowsContainer');
    if (!container) return;

    if (!rows || rows.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 60px 20px; color: var(--text-muted);">
          <h3>No items match current filters</h3>
        </div>
      `;
      return;
    }

    container.innerHTML = rows.map(row => {
      let filteredItems = row.items;
      if (this.currentCategoryFilter === 'movies') {
        filteredItems = filteredItems.filter(i => i.type === 'movie');
      } else if (this.currentCategoryFilter === 'books') {
        filteredItems = filteredItems.filter(i => i.type === 'book');
      }

      if (filteredItems.length === 0) return '';

      return `
        <section class="stream-row-section">
          <div class="row-header">
            <div class="row-title-box">
              <h2 class="row-title">${row.title}</h2>
              <span class="row-subtitle">&bull; ${row.subtitle}</span>
            </div>
          </div>

          <button class="carousel-btn left" onclick="App.scrollRow('${row.id}', -1)" title="Scroll Left">&#8249;</button>
          
          <div class="row-carousel-container" id="carousel_${row.id}">
            <div class="carousel-track">
              ${filteredItems.map(item => this.createCardHTML(item)).join('')}
            </div>
          </div>

          <button class="carousel-btn right" onclick="App.scrollRow('${row.id}', 1)" title="Scroll Right">&#8250;</button>
        </section>
      `;
    }).join('');
  },

  scrollRow(rowId, direction) {
    const el = document.getElementById(`carousel_${rowId}`);
    if (el) {
      const scrollAmount = (el.clientWidth || 600) * 0.75 * direction;
      el.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
  },

  createCardHTML(item) {
    const isSaved = this.myWatchlist.includes(item.id);

    return `
      <div class="stream-card" onclick="App.openItemModal('${item.id}')">
        <div class="card-poster-wrapper">
          <img src="${item.poster}" alt="${item.title}" class="card-poster" loading="lazy" />
          <div class="card-overlay-gradient"></div>
          
          <span class="card-match-tag">${item.confidence || 95}% Match</span>
          <span class="card-type-tag">${item.type}</span>

          <div class="card-info-bottom">
            <div class="card-title">${item.title}</div>
            <div class="card-meta-row">
              <span class="card-rating-star">★ ${item.rating}</span>
              <span>&bull;</span>
              <span>${item.year}</span>
              <span>&bull;</span>
              <span>${item.runtime_or_pages}</span>
            </div>

            <div class="card-hover-actions" onclick="event.stopPropagation()">
              <button class="btn-circle-action primary" onclick="App.playItem('${item.id}')" title="Play">
                ▶
              </button>
              <button class="btn-circle-action" onclick="App.toggleWatchlist('${item.id}', this)" title="${isSaved ? 'Remove from List' : 'Add to List'}">
                ${isSaved ? '✓' : '➕'}
              </button>
              <button class="btn-circle-action" onclick="App.openItemModal('${item.id}')" title="More Info & AI Trace">
                ℹ
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  async openItemModal(itemId) {
    const modal = document.getElementById('streamModal');
    const modalContent = document.getElementById('streamModalContent');
    if (!modal || !modalContent) return;

    modal.classList.add('open');
    modalContent.innerHTML = `
      <div style="padding: 60px; text-align: center; color: var(--text-muted);">
        <div style="font-size: 2rem; margin-bottom: 12px;">⚙</div>
        <p>Loading title details & AI derivation trace...</p>
      </div>
    `;

    try {
      const res = await fetch('/api/explain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ item_id: itemId, user_facts: this.facts })
      });
      const json = await res.json();

      if (json.success && json.data) {
        const exp = json.data;
        const item = exp.item;
        const isSaved = this.myWatchlist.includes(item.id);

        modalContent.innerHTML = `
          <div class="modal-header-hero" style="background-image: url('${item.backdrop || item.poster}');">
            <div class="modal-header-gradient"></div>
            <button class="modal-close-icon" onclick="App.closeItemModal()">&times;</button>
            <div class="modal-hero-title-box">
              <h2 class="modal-title">${item.title}</h2>
              <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 14px;">
                <button class="btn-play-hero" onclick="App.playItem('${item.id}')">
                  <span>▶</span> Play Preview
                </button>
                <button class="btn-circle-action" style="width: 44px; height: 44px;" onclick="App.toggleWatchlist('${item.id}', this)">
                  ${isSaved ? '✓' : '➕'}
                </button>
              </div>
            </div>
          </div>

          <div class="modal-body-layout">
            <!-- Left: Metadata & Story -->
            <div class="modal-left-col">
              <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                <span class="match-percentage-badge">${exp.confidence}% Match</span>
                <span style="color: var(--text-muted);">${item.year}</span>
                <span class="streaming-quality-badge">${item.age_rating || '16+'}</span>
                <span class="streaming-quality-badge">${item.runtime_or_pages}</span>
                <span class="streaming-quality-badge">${item.quality || '4K Ultra HD'}</span>
              </div>

              <p style="font-size: 1rem; color: #e5e5e5; line-height: 1.6;">${item.synopsis}</p>

              <div style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.8;">
                <div><span style="color: var(--text-muted);">Creator:</span> ${item.director_or_author}</div>
                ${item.cast ? `<div><span style="color: var(--text-muted);">Cast / Notables:</span> ${item.cast.join(', ')}</div>` : ''}
                <div><span style="color: var(--text-muted);">Genres:</span> ${item.genres.join(', ')}</div>
                <div><span style="color: var(--text-muted);">Where to Experience:</span> ${item.streaming_or_publisher}</div>
              </div>
            </div>

            <!-- Right: FlixMatch AI Reasoning & Cross-Media -->
            <div class="modal-right-col">
              <div style="font-family: var(--font-display); font-size: 1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center; gap: 6px;">
                <span>🧠</span> Why FlixMatch AI Picked This
              </div>

              ${exp.supporting_rules.length > 0 ? `
                <div class="ai-proof-card">
                  <div style="font-weight: 700; color: #00d2ff; margin-bottom: 4px;">
                    ${exp.supporting_rules[0].name}
                  </div>
                  <div>${exp.supporting_rules[0].explanation}</div>
                </div>
              ` : `
                <div class="ai-proof-card">
                  Matched your ${this.facts.mood} mood and preferred pace.
                </div>
              `}

              <!-- Cross Media Link -->
              ${exp.cross_media_item ? `
                <div style="margin-top: 10px;">
                  <div style="font-size: 0.78rem; font-family: var(--font-mono); text-transform: uppercase; color: var(--text-dim); margin-bottom: 6px;">
                    Companion ${exp.cross_media_item.type === 'book' ? '📖 Book Recommendation' : '🎬 Movie Recommendation'}:
                  </div>
                  <div class="cross-rec-box" onclick="App.openItemModal('${exp.cross_media_item.id}')">
                    <img src="${exp.cross_media_item.poster}" class="cross-rec-thumb" alt="${exp.cross_media_item.title}">
                    <div>
                      <div style="font-weight: 700; font-size: 0.9rem; color: #ffffff;">${exp.cross_media_item.title}</div>
                      <div style="font-size: 0.78rem; color: var(--text-muted);">${exp.cross_media_item.director_or_author}</div>
                    </div>
                  </div>
                </div>
              ` : ''}
            </div>
          </div>
        `;
      }
    } catch (err) {
      modalContent.innerHTML = `<div style="padding: 40px; color: var(--netflix-red);">Error loading title: ${err.message}</div>`;
    }
  },

  closeItemModal() {
    const modal = document.getElementById('streamModal');
    if (modal) modal.classList.remove('open');
  },

  playItem(itemId) {
    const item = this.allRecommendations.find(i => i.id === itemId) || this.currentHeroItem;
    if (item) {
      alert(`▶ Streaming "${item.title}" now on ${item.streaming_or_publisher}!`);
    }
  },

  toggleWatchlist(itemId, btnEl) {
    const idx = this.myWatchlist.indexOf(itemId);
    if (idx > -1) {
      this.myWatchlist.splice(idx, 1);
      if (btnEl) btnEl.textContent = '➕';
    } else {
      this.myWatchlist.push(itemId);
      if (btnEl) btnEl.textContent = '✓';
    }
    localStorage.setItem('flixmatch_watchlist', JSON.stringify(this.myWatchlist));

    if (this.currentCategoryFilter === 'watchlist') {
      this.showWatchlist();
    }
  },

  updateHeroWatchlistButton(itemId) {
    const btn = document.getElementById('btnHeroWatchlist');
    if (!btn) return;
    const isSaved = this.myWatchlist.includes(itemId);
    btn.innerHTML = `<span>${isSaved ? '✓' : '➕'}</span> ${isSaved ? 'In My List' : 'My List'}`;
    btn.onclick = () => {
      this.toggleWatchlist(itemId);
      this.updateHeroWatchlistButton(itemId);
    };
  },

  filterCategory(category) {
    this.currentCategoryFilter = category;
    if (category === 'watchlist') {
      this.showWatchlist();
    } else if (category === 'top_picks') {
      const topRow = document.querySelector('.stream-row-section');
      if (topRow) topRow.scrollIntoView({ behavior: 'smooth' });
    } else {
      this.fetchRecommendations();
    }
  },

  showWatchlist() {
    const container = document.getElementById('streamingRowsContainer');
    if (!container) return;

    const savedItems = this.allRecommendations.filter(i => this.myWatchlist.includes(i.id));

    if (savedItems.length === 0) {
      container.innerHTML = `
        <div style="padding: 80px 20px; text-align: center; color: var(--text-muted);">
          <h2>Your Watchlist is Empty</h2>
          <p style="margin-top: 8px;">Explore recommendations and click ➕ to save movies and books to your list.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <section class="stream-row-section">
        <div class="row-header">
          <div class="row-title-box">
            <h2 class="row-title">My Saved List (${savedItems.length})</h2>
          </div>
        </div>
        <div class="row-carousel-container">
          <div class="carousel-track" style="flex-wrap: wrap;">
            ${savedItems.map(item => this.createCardHTML(item)).join('')}
          </div>
        </div>
      </section>
    `;
  },

  async handleSearch(query) {
    if (!query || query.trim() === '') {
      this.fetchRecommendations();
      return;
    }

    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query.trim())}`);
      const data = await res.json();
      if (data.success) {
        const container = document.getElementById('streamingRowsContainer');
        if (!container) return;

        if (data.results.length === 0) {
          container.innerHTML = `
            <div style="padding: 80px 20px; text-align: center; color: var(--text-muted);">
              <h3>No results found for "${query}"</h3>
            </div>
          `;
          return;
        }

        container.innerHTML = `
          <section class="stream-row-section">
            <div class="row-header">
              <div class="row-title-box">
                <h2 class="row-title">Search Results for "${query}" (${data.results.length})</h2>
              </div>
            </div>
            <div class="row-carousel-container">
              <div class="carousel-track" style="flex-wrap: wrap;">
                ${data.results.map(item => this.createCardHTML(item)).join('')}
              </div>
            </div>
          </section>
        `;
      }
    } catch (err) {
      console.error(err);
    }
  }
};

window.addEventListener('DOMContentLoaded', () => {
  App.init();
});
